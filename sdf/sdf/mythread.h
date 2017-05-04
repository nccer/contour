#ifndef MYTHREAD_H
#define MYTHREAD_H

#include<QThread>

class Mythread : public QThread
{
    Q_OBJECT
public:
    Mythread();

protected:
    void run();
public:
    QStringList titleListInSDF1;
    QStringList titleListInSDF2;
    QStringList titleListInSDF;
    QStringList titleListInCSV;
    void setString(QString str1, QString str2, QString str3, QString str4, bool isGen);

private:
    bool comma;
    int count;
    int successCount;
    QString sdfa;
    QString sdfcsv;
    QString molf;
    QString resu;

private:
    QStringList splitLine(QString line);
    QStringList titleInSDF(QStringList sdfTitleList, QString path);
    QStringList titleInCSV(QString path);
    bool isGen;

    void tGenerateSDF(QString str1, QString str2, QString str3, QString str4);
    void tMergeSDF(QString str1, QString str2, QString str3);

signals:
    void err(QString err);
    void suc(QString succ);

public slots:

};

#endif // MYTHREAD_H
