#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QtQml>
#include "sdf.h"

int main(int argc, char *argv[])
{
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
    QGuiApplication app(argc, argv);

    Sdf sdf;
    //qmlRegisterType<Sdf>("Sdf", 1, 0, "Sdf");
    QQmlApplicationEngine engine;
    engine.rootContext()->setContextProperty("sdf", &sdf);
    engine.rootContext()->setContextProperty("threadA", &sdf.threadA);
    engine.rootContext()->setContextProperty("threadB", &sdf.threadB);
    engine.load(QUrl(QLatin1String("qrc:/main.qml")));

    return app.exec();
}
