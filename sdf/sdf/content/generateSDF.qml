import QtQuick 2.7
import QtQuick.Controls 2.1
import QtQuick.Layouts 1.2
import QtQuick.Controls.Material 2.1
import QtQml.Models 2.2
import QtQuick.Dialogs 1.2


Item {
    id: mainItem
    anchors.fill: parent

    Connections {
        target: threadA
        onErr: {
            generateButton.enabled = true
            successLabel.state = "fail"
        }
        onSuc: {
            generateButton.enabled = true
            successLabel.state = "succ"
        }
    }
    Label {
        id: titleLabel
        text: qsTr("修改sdf文件")
        anchors.left: mainItem.left
        anchors.leftMargin: 200
        anchors.top: mainItem.top
        anchors.topMargin: 20
        font.pixelSize: 40

    }
    Label {
        id: sdfLabel
        text: qsTr("输入sdf文件地址")
        anchors.left: mainItem.left
        anchors.leftMargin: 100
        anchors.top: titleLabel.top
        anchors.topMargin: 80
        font.pixelSize: 20

    }
    TextField {
        id: sdfTextfield
        anchors.top: sdfLabel.bottom
        anchors.topMargin: 8
        anchors.left: sdfLabel.left
        width: 300
        placeholderText: qsTr("sdf文件地址")
    }
    Button {
        id: sdfButton
        anchors.left: sdfTextfield.right
        anchors.leftMargin: 80
        anchors.bottom: sdfTextfield.bottom
        width: 100
        text: qsTr("浏览sdf文件")
        onClicked: sdfDialog.open()
    }
    Label {
        id: csvLabel
        text: qsTr("输入csv文件地址")
        anchors.left: sdfLabel.left
        anchors.top: sdfTextfield.top
        anchors.topMargin: 40
        font.pixelSize: 20

    }
    TextField {
        id: csvTextfield
        anchors.top: csvLabel.bottom
        anchors.topMargin: 8
        anchors.left: sdfLabel.left
        width: 300
        placeholderText: qsTr("csv文件地址")
    }
    Button {
        id: csvButton
        anchors.left: csvTextfield.right
        anchors.leftMargin: 80
        anchors.bottom: csvTextfield.bottom
        width: 100
        text: qsTr("浏览csv文件")
        onClicked: csvDialog.open()
    }
    Label {
        id: molLabel
        text: qsTr("输入mol文件夹地址")
        anchors.left: sdfLabel.left
        anchors.top: csvTextfield.top
        anchors.topMargin: 40
        font.pixelSize: 20

    }
    TextField {
        id: molTextfield
        anchors.top: molLabel.bottom
        anchors.topMargin: 8
        anchors.left: sdfLabel.left
        width: 300
        placeholderText: qsTr("mol文件夹地址")
    }
    Button {
        id: molButton
        anchors.left: molTextfield.right
        anchors.leftMargin: 80
        anchors.bottom: molTextfield.bottom
        width: 100
        text: qsTr("mol文件夹")
        onClicked: molDialog.open()
    }
    Label {
        id: resultLabel
        text: qsTr("文件保存到哪里")
        anchors.left: sdfLabel.left
        anchors.top: molTextfield.top
        anchors.topMargin: 40
        font.pixelSize: 20

    }
    TextField {
        id: resultTextfield
        anchors.top: resultLabel.bottom
        anchors.topMargin: 8
        anchors.left: sdfLabel.left
        width: 300
        placeholderText: qsTr("请输入保存文件位置")
    }
    Button {
        id: resultButton
        anchors.left: resultTextfield.right
        anchors.leftMargin: 80
        anchors.bottom: resultTextfield.bottom
        width: 100
        text: qsTr("浏览文件夹")
        onClicked: fileDialog.open()
    }
    Label {
        id: successLabel
        anchors.left: sdfLabel.left
        anchors.leftMargin: -20
        anchors.bottomMargin: -50
        anchors.bottom: pushButton.bottom
        font.pixelSize: 20
        states: [
            State {
                name: "succ"
                PropertyChanges {
                    target: successLabel
                    text: qsTr("成功的生成了新的sdf文件!")
                }
            },
            State {
                name: "fail"
                PropertyChanges {
                    target: successLabel
                    text: qsTr("失败了,请检查SDF文件条目和CSV标题是否匹配!")
                }
            },
            State {
                name: "busy"
                PropertyChanges {
                    target: successLabel
                    text: qsTr("正在生成,请稍等.")
                }
            },
            State {
                name: "norm"
                PropertyChanges {
                    target: successLabel
                    text: qsTr("")
                }
            }
        ]
        state: "norm"
    }

    Button {
        id: generateButton
        anchors.top: resultButton.bottom
        anchors.topMargin: 40
        anchors.left: resultButton.left
        width: 100
        text: qsTr("生成")
        Material.background: Material.Orange
        Material.accent: "#f0f0f0"
        Material.foreground: "#f0f0f0"
        onClicked: {
            successLabel.state = "busy"
            generateButton.enabled = false
            sdf.generateSDF(sdfTextfield.text, csvTextfield.text, molTextfield.text, resultTextfield.text)
        }
    }

    Button {
        id: pushButton
        anchors.top: generateButton.top
        anchors.right: generateButton.left
        anchors.rightMargin: 40
        width: 100
        text: qsTr("合并sdf")
        Material.background: Material.Blue
        Material.accent: "#f0f0f0"
        Material.foreground: "#f0f0f0"
        onClicked: {
           stack.push(popView)
        }
    }

    FileDialog {
        id: sdfDialog
        visible: false
        title: qsTr("请选择一个文件")
        folder: shortcuts.home
        nameFilters: [ "SDF,CSV files (*.sdf *.csv)", "All files (*)" ]
        onAccepted: {
            sdfTextfield.text = sdfDialog.fileUrl.toString().substring(8)
        }
        onRejected: {
            console.log("Canceled")
        }
    }
    FileDialog {
        id: csvDialog
        visible: false
        title: qsTr("请选择一个文件")
        folder: shortcuts.home
        nameFilters: [ "SDF,CSV files (*.sdf *.csv)", "All files (*)" ]
        onAccepted: {
            csvTextfield.text = csvDialog.fileUrl.toString().substring(8)
        }
        onRejected: {
            console.log("Canceled")
        }
    }
    FileDialog {
        id: molDialog
        visible: false
        title: qsTr("请选择一个文件夹")
        folder: shortcuts.home
        selectFolder: true
        onAccepted: {
            molTextfield.text = molDialog.fileUrl.toString().substring(8)
        }
        onRejected: {
            console.log("Canceled")
        }
    }
    FileDialog {
        id: fileDialog
        visible: false
        title: qsTr("请选择一个文件夹")
        folder: shortcuts.home
        selectFolder: true
        onAccepted: {
            resultTextfield.text = fileDialog.fileUrl.toString().substring(8)
        }
        onRejected: {
            console.log("Canceled")
        }
    }
}
