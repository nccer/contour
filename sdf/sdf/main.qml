import QtQuick 2.7
import QtQuick.Controls 2.1
import QtQuick.Layouts 1.2
import QtQml.Models 2.2
import "./content"


ApplicationWindow {
    visible: true
    width: 640
    height: 560
    maximumWidth: 640
    maximumHeight: 560
    minimumWidth: 640
    minimumHeight: 560
    title: qsTr("修改sdf文件")

    StackView {
        id: stack
        initialItem: mainView
        anchors.fill: parent
    }
    Component {
        id: mainView
        Loader {
            source: "./content/generateSDF.qml"
        }
    }
    Component {
        id: popView
        Loader {
            Loader {
                source: "./content/mergeSDF.qml"
            }
        }
    }
}
