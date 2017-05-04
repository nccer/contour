#ifndef SDF_H
#define SDF_H

#include <QObject>
#include "mythread.h"

class QStringList;
class QThread;

class Sdf : public QObject
{
    Q_OBJECT
public:
    explicit Sdf(QObject *parent = 0);

public:
    Mythread threadA;
    Mythread threadB;

private:
    QStringList splitLine(QString line);
    QStringList titleInSDF(QStringList sdfTitleList, QString path);
    QStringList titleInCSV(QString path);

signals:

public slots:
    void generateSDF(QString str1, QString str2, QString str3, QString str4);
    void mergeSDF(QString str1, QString str2, QString str3);
};

#endif // SDF_H
