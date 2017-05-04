import QtQuick 2.7
import QtQuick.Controls 2.1
import QtQuick.Controls.Material 2.1
import QtQuick.Dialogs 1.2

Item {
    id: mergemainItem
    anchors.fill: parent

    Connections {
        target: threadB
        onErr: {
            mergegenerateButton.enabled = true
            mergesuccessLabel.state = "fail"
        }
        onSuc: {
            mergegenerateButton.enabled = true
            mergesuccessLabel.state = "succ"
        }
    }

    Label {
        id: mergetitleLabel
        text: qsTr("合并sdf文件")
        anchors.left: mergemainItem.left
        anchors.leftMargin: 200
        anchors.top: mergemainItem.top
        anchors.topMargin: 20
        font.pixelSize: 40

    }
    Label {
        id: mergesdfLabel
        text: qsTr("输入第一个sdf文件地址")
        anchors.left: mergemainItem.left
        anchors.leftMargin: 100
        anchors.top: mergetitleLabel.bottom
        anchors.topMargin: 80
        font.pixelSize: 20

    }
    TextField {
        id: mergesdfTextfield
        anchors.top: mergesdfLabel.bottom
        anchors.topMargin: 8
        anchors.left: mergesdfLabel.left
        width: 300
        placeholderText: qsTr("sdf文件地址")
    }
    Button {
        id: mergesdfButton
        anchors.left: mergesdfTextfield.right
        anchors.leftMargin: 80
        anchors.bottom: mergesdfTextfield.bottom
        width: 100
        text: qsTr("浏览sdf文件")
        onClicked: mergesdfDialog.open()
    }
    Label {
        id: mergecsvLabel
        text: qsTr("输入第二个sdf文件地址")
        anchors.left: mergesdfLabel.left
        anchors.top: mergesdfTextfield.top
        anchors.topMargin: 40
        font.pixelSize: 20

    }
    TextField {
        id: mergecsvTextfield
        anchors.top: mergecsvLabel.bottom
        anchors.topMargin: 8
        anchors.left: mergesdfLabel.left
        width: 300
        placeholderText: qsTr("sdf文件地址")
    }
    Button {
        id: mergecsvButton
        anchors.left: mergecsvTextfield.right
        anchors.leftMargin: 80
        anchors.bottom: mergecsvTextfield.bottom
        width: 100
        text: qsTr("浏览sdf文件")
        onClicked: mergecsvDialog.open()
    }
    Label {
        id: mergemolLabel
        text: qsTr("文件保存到哪里")
        anchors.left: mergesdfLabel.left
        anchors.top: mergecsvTextfield.top
        anchors.topMargin: 40
        font.pixelSize: 20

    }
    TextField {
        id: mergeresultTextfield
        anchors.top: mergemolLabel.bottom
        anchors.topMargin: 8
        anchors.left: mergesdfLabel.left
        width: 300
        placeholderText: qsTr("请输入保存文件位置")
    }
    Button {
        id: mergeresultButton
        anchors.left: mergeresultTextfield.right
        anchors.leftMargin: 80
        anchors.bottom: mergeresultTextfield.bottom
        width: 100
        text: qsTr("浏览文件夹")
        onClicked: mergeresultDialog.open()
    }
    Label {
        id: mergesuccessLabel
        anchors.left: mergesdfLabel.left
        anchors.leftMargin: -20
        anchors.bottomMargin: -50
        anchors.bottom: popButton.bottom
        font.pixelSize: 20
        states: [
            State {
                name: "succ"
                PropertyChanges {
                    target: mergesuccessLabel
                    text: qsTr("成功的生成了新的sdf文件!")
                }
            },
            State {
                name: "fail"
                PropertyChanges {
                    target: mergesuccessLabel
                    text: qsTr("失败了,请检查两个SDF的条目是否相同")
                }
            },
            State {
                name: "busy"
                PropertyChanges {
                    target: mergesuccessLabel
                    text: qsTr("正在生成,请稍等.")
                }
            },
            State {
                name: "norm"
                PropertyChanges {
                    target: mergesuccessLabel
                    text: qsTr("")
                }
            }
        ]
        state: "norm"
    }

    Button {
        id: popButton
        anchors.top: mergegenerateButton.top
        anchors.right: mergegenerateButton.left
        anchors.rightMargin: 40
        width: 100
        text: qsTr("修改sdf")
        Material.background: Material.Blue
        Material.accent: "#f0f0f0"
        Material.foreground: "#f0f0f0"
        onClicked: {
            stack.pop()
        }
    }
    Button {
        id: mergegenerateButton
        anchors.bottom: mergemainItem.bottom
        anchors.bottomMargin: -460
        anchors.left: mergeresultButton.left
        width: 100
        text: qsTr("生成")
        Material.background: Material.Orange
        Material.accent: "#f0f0f0"
        Material.foreground: "#f0f0f0"
        onClicked: {
            mergesuccessLabel.state = "busy"
            mergegenerateButton.enabled = false
            sdf.mergeSDF(mergesdfTextfield.text, mergecsvTextfield.text, mergeresultTextfield.text)
        }
    }
    FileDialog {
        id: mergesdfDialog
        visible: false
        title: qsTr("请选择一个文件")
        folder: shortcuts.home
        nameFilters: [ "SDF,CSV files (*.sdf *.csv)", "All files (*)" ]
        onAccepted: {
            mergesdfTextfield.text = mergesdfDialog.fileUrl.toString().substring(8)
        }
        onRejected: {
            console.log("Canceled")
        }
    }
    FileDialog {
        id: mergecsvDialog
        visible: false
        title: qsTr("请选择一个文件")
        folder: shortcuts.home
        nameFilters: [ "SDF,CSV files (*.sdf *.csv)", "All files (*)" ]
        onAccepted: {
            mergecsvTextfield.text = mergecsvDialog.fileUrl.toString().substring(8)
        }
        onRejected: {
            console.log("Canceled")
        }
    }
    FileDialog {
        id: mergeresultDialog
        visible: false
        title: qsTr("请选择一个文件夹")
        folder: shortcuts.home
        selectFolder: true
        onAccepted: {
            mergeresultTextfield.text = mergeresultDialog.fileUrl.toString().substring(8)
        }
        onRejected: {
            console.log("Canceled")
        }
    }
}
