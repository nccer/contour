#include "mythread.h"
#include <QDebug>
#include <QFile>
#include <QList>

Mythread::Mythread() : comma(false), count(0), successCount(0)
{
    titleListInSDF = QStringList();
    titleListInSDF1 = QStringList();
    titleListInSDF2 = QStringList();
    titleListInCSV = QStringList();
}

void Mythread::tGenerateSDF(QString str1, QString str2, QString str3, QString str4) {
    QString casRegistryNumber("CAS");
    QFile sdf(str1);
    QFile csv(str2);
    QFile result(str4 + "\\result.sdf");
    QFile missingFile(str4 + "\\log.txt");
    QFile lostFile(str4 + "\\lost.csv");
    QList<QString> casList;
    QList<QString> missingcasList;
    this->titleListInSDF = titleInSDF(this->titleListInSDF, str1);
    this->titleListInCSV = titleInCSV(str2);
    foreach (QString sdfTitle, this->titleListInSDF) {
        if(this->titleListInCSV.indexOf(sdfTitle) == -1) {
            emit err("SDF文件和CSV文件的标题不匹配");
            return;
        }
    }

    if(sdf.open(QIODevice::ReadOnly | QIODevice::Text)) {
        QTextStream sdfStream(&sdf);
        QString sdfLine = sdfStream.readLine();
        if(result.open(QIODevice::WriteOnly | QIODevice::Append | QIODevice::Text)) {
            QTextStream resultStream(&result);
            while(!sdfLine.isNull()) {
                resultStream<<sdfLine<<"\n";
                if(sdfLine.indexOf(casRegistryNumber) != -1) {
                    sdfLine = sdfStream.readLine();
                    casList<<sdfLine;
                } else {
                    sdfLine = sdfStream.readLine();
                }
            }
        }
        result.close();
    }
    sdf.close();
    if(csv.open(QIODevice::ReadOnly | QIODevice::Text)) {
        QTextStream csvStream(&csv);
        QString csvLine = csvStream.readLine();
        QStringList titleList = splitLine(csvLine);
        int casLocate = 0;
        bool isFindCAS = false;
        lostFile.open(QIODevice::WriteOnly | QIODevice::Append | QIODevice::Text);
        QTextStream lostFileStream(&lostFile);
        foreach(QString item, titleList) {
            if(item.indexOf(casRegistryNumber) != -1) {
                casLocate = titleList.indexOf(item);
                isFindCAS = true;
            }
        }
        lostFileStream<<csvLine<<"\n";
        csvLine = csvStream.readLine();
        if(isFindCAS) {
            while(!csvLine.isNull()) {
                QStringList varList = splitLine(csvLine);
                if(casList.indexOf(varList.at(casLocate)) != -1) {
                    this->count += 1;
                    csvLine = csvStream.readLine();
                    continue;
                }
                QString molFileName(str3 + "\\" + varList.at(casLocate) + ".mol");
                QFile mol(molFileName);
                if(mol.open(QIODevice::ReadOnly | QIODevice::Text)) {
                    QTextStream molStream(&mol);
                    QString molLine = molStream.readLine();
                    if(result.open(QIODevice::WriteOnly | QIODevice::Append | QIODevice::Text)) {
                        QTextStream resultStream(&result);
                        while(!molLine.isNull()) {
                            resultStream<<molLine<<"\n";
                            molLine = molStream.readLine();
                        }
                        foreach (QString va_arg, titleList) {
                            QString titleString(">  <" + va_arg + ">\n");
                            QString valueString(varList.at(titleList.indexOf(va_arg)) + "\n");
                            resultStream<<titleString;
                            resultStream<<valueString;
                            resultStream<<"\n";
                        }
                        resultStream<<"$$$$\n";
                        this->successCount += 1;
                    }
                } else {
                    lostFileStream<<csvLine<<"\n";
                    missingcasList<<varList.at(casLocate);
                }
                result.close();
                mol.close();
                csvLine = csvStream.readLine();
            }
        }
        lostFile.close();
    }
    csv.close();
//    if(missingFile.open(QIODevice::WriteOnly | QIODevice::Append | QIODevice::Text)) {
//        QTextStream missingcasStream(&missingFile);
//        missingcasStream<<QString("本次共导入了")<<missingcasList.count() + this->count + this->successCount<<QString("个分子。");
//        missingcasStream<<QString("其中，成功")<<this->successCount<<QString("个分子。失败")<< this->count + missingcasList.count()<<QString("个分子。\n");
//        missingcasStream<<QString("有")<<this->count<<QString("个分子已存在，毋须导入。有")<< missingcasList.count()<<QString("个分子缺少mol文件,列表如下：\n\n");
//        foreach (QString casNumber, missingcasList) {
//            missingcasStream<<casNumber<<"\n";
//        }
//    }
//    missingFile.close();
    this->successCount = 0;
    this->count = 0;
    emit suc("成功生成SDF");
}

QStringList Mythread::splitLine(QString line) {
    QStringList priStringList = line.split(",");
    QStringList resultStringList;
    QString commaString;
    foreach (QString item, priStringList) {
        if(item.indexOf("\"") != -1) {
            if(this->comma) {
                this->comma = false;
                commaString += "," + item.remove("\"");
                resultStringList<<commaString;
            } else {
                this->comma = true;
                commaString += item.remove("\"");
            }
        } else {
            if(this->comma) {
                commaString += "," + item;
            } else {
                resultStringList<<item;
            }
        }
    }
    return resultStringList;
}

void Mythread::tMergeSDF(QString str1, QString str2, QString str3) {

    this->titleListInSDF1 = titleInSDF(this->titleListInSDF1, str1);
    this->titleListInSDF2 = titleInSDF(this->titleListInSDF2, str2);
    foreach (QString title, this->titleListInSDF1) {
        if(this->titleListInSDF2.indexOf(title) == -1) {
//            emit err("两个SDF文件条目不匹配");
            return;
        }
    }


    QString casRegistryNumber("CAS");
    QString dollorFlag("$$$$");
    QString casNumber;
    bool isFound = true;
    QFile sdf(str1);
    QFile sdf2(str2);
    QFile result(str3 + "/result.sdf");
    QList<QString> casList;
    QList<QString> stringBuffer;
    if(sdf.open(QIODevice::ReadOnly | QIODevice::Text)) {
        QTextStream sdfStream(&sdf);
        QString sdfLine = sdfStream.readLine();
        if(result.open(QIODevice::WriteOnly | QIODevice::Append | QIODevice::Text)) {
            QTextStream resultStream(&result);
            while(!sdfLine.isNull()) {
                resultStream<<sdfLine<<"\n";
                if(sdfLine.indexOf(casRegistryNumber) != -1) {
                    sdfLine = sdfStream.readLine();
                    casList<<sdfLine;
                } else {
                    sdfLine = sdfStream.readLine();
                }
            }
        }
    }
    sdf.close();
    result.close();
    if(sdf2.open(QIODevice::ReadOnly | QIODevice::Text)) {
        QTextStream sdf2Stream(&sdf2);
        QString sdf2Line = sdf2Stream.readLine();
        if(result.open(QIODevice::WriteOnly | QIODevice::Append | QIODevice::Text)) {
            QTextStream resultStream(&result);
            while(!sdf2Line.isNull()) {
                if(sdf2Line.indexOf(casRegistryNumber) != -1) {
                    sdf2Line  = sdf2Stream.readLine();
                    casNumber = sdf2Line;
                } else {
                    sdf2Line = sdf2Stream.readLine();
                }
                stringBuffer<<sdf2Line;
                if(sdf2Line.indexOf(dollorFlag) != -1) {
                    isFound = false;
                    foreach (QString line, casList) {
                        if(line.indexOf(casNumber) != -1) {
                            isFound = true;
                            break;
                        }
                    }
                    if(isFound) {
                        foreach (QString line, stringBuffer) {
                            stringBuffer.removeOne(line);
                        }
                    } else {
                        foreach (QString line, stringBuffer) {
                            resultStream<<line<<"\n";
                            stringBuffer.removeOne(line);
                        }
                    }
                }
            }
        }
        result.close();
    }
    sdf2.close();
    emit suc("成功合并SDF");
}

QStringList Mythread::titleInSDF(QStringList sdfTitleList, QString path) {
    foreach (QString line, sdfTitleList) {
        sdfTitleList.removeOne(line);
    }
    QFile sdf(path);
    if(sdf.open(QIODevice::ReadOnly | QIODevice::Text)) {
        QTextStream sdfStream(&sdf);
        QString line = sdfStream.readLine();
        while(!line.isNull()) {
            sdfTitleList<<line;
            if(line.indexOf("$$$$") != -1) {
                break;
            }
            line = sdfStream.readLine();
        }
        sdf.close();
    }
    foreach (QString tline, sdfTitleList) {
        if(tline.at(0) == ">") {
            QString title = tline.mid(tline.indexOf("<") + 1);
            int i = title.indexOf(">");
            i -= 1;
            title = title.mid(0, i);
            sdfTitleList.append(title);
            sdfTitleList.removeOne(tline);
        } else {
            sdfTitleList.removeOne(tline);
        }
    }
    return sdfTitleList;
}

QStringList Mythread::titleInCSV(QString path) {
    foreach (QString line, this->titleListInCSV) {
        this->titleListInCSV.removeOne(line);
    }
    QFile csv(path);
    if(csv.open(QIODevice::ReadOnly | QIODevice::Text)) {
        QTextStream csvStream(&csv);
        QString line = csvStream.readLine();
        if(!line.isNull()) {
            this->titleListInCSV = splitLine(line);
        }
    }
    return this->titleListInCSV;
}

void Mythread::run() {
    if(this->isGen) {
        tGenerateSDF(sdfa, sdfcsv, molf, resu);
    } else {
        qDebug()<<"tmerS";
        tMergeSDF(sdfa, sdfcsv, molf);
        qDebug()<<"tMere";
    }

}
void Mythread::setString(QString str1, QString str2, QString str3, QString str4, bool isGen) {
    this->sdfa = str1;
    this->sdfcsv = str2;
    this->molf = str3;
    this->resu = str4;
    this->isGen = isGen;
    this->start();
    qDebug()<<"run";
}
