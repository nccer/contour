#include "sdf.h"
#include <QDebug>
#include <QFile>
#include <QList>

Sdf::Sdf(QObject *parent) : QObject(parent)
{

}

void Sdf::generateSDF(QString str1, QString str2, QString str3, QString str4) {
    qDebug()<<"gen";
    threadA.setString(str1, str2, str3, str4, true);
}
void Sdf::mergeSDF(QString str1, QString str2, QString str3) {
    qDebug()<<"mer";
    threadB.setString(str1, str2, str3, "", false);
}
