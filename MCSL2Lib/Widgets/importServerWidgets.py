from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtWidgets import (
    QSpacerItem,
    QVBoxLayout,
    QSizePolicy,
    QWidget,
    QGridLayout,
    QHBoxLayout,
)
from qfluentwidgets import (
    CardWidget,
    ComboBox,
    HorizontalSeparator,
    LineEdit,
    PixmapLabel,
    PlainTextEdit,
    PrimaryPushButton,
    PushButton,
    StrongBodyLabel,
    SubtitleLabel,
    TextEdit,
    TransparentToolButton,
    BodyLabel,
)

from MCSL2Lib.Controllers.interfaceController import MySmoothScrollArea


class ImportPageWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("importPageWidget")
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.backToMain = TransparentToolButton(self)
        self.backToMain.setObjectName("backToMain")
        self.gridLayout.addWidget(self.backToMain, 0, 1, 1, 1)
        self.importPageTitle = SubtitleLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.importPageTitle.sizePolicy().hasHeightForWidth()
        )
        self.importPageTitle.setSizePolicy(sizePolicy)
        self.importPageTitle.setObjectName("importPageTitle")
        self.gridLayout.addWidget(self.importPageTitle, 0, 2, 1, 1)
        spacerItem = QSpacerItem(619, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QSpacerItem(20, 449, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.importScrollArea = MySmoothScrollArea(self)
        self.importScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.importScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.importScrollArea.setWidgetResizable(True)
        self.importScrollArea.setAlignment(Qt.AlignCenter)
        self.importScrollArea.setObjectName("importScrollArea")
        self.importScrollAreaWidgetContents = QWidget()
        self.importScrollAreaWidgetContents.setGeometry(QRect(0, 0, 742, 452))
        self.importScrollAreaWidgetContents.setObjectName(
            "importScrollAreaWidgetContents"
        )
        self.verticalLayout_2 = QVBoxLayout(self.importScrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.importScrollArea.setWidget(self.importScrollAreaWidgetContents)
        self.gridLayout.addWidget(self.importScrollArea, 1, 2, 1, 2)
        spacerItem2 = QSpacerItem(20, 478, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 2, 1)

        # self.importPageTitle.setText("[Import Type Title]")


class ConfirmArgumentsWidget(CardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("confirmArgumentsWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(0, 650))
        self.setMaximumSize(QSize(16777215, 650))
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.statusIcon = PixmapLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusIcon.sizePolicy().hasHeightForWidth())
        self.statusIcon.setSizePolicy(sizePolicy)
        self.statusIcon.setMinimumSize(QSize(30, 30))
        self.statusIcon.setMaximumSize(QSize(30, 30))
        self.statusIcon.setObjectName("statusIcon")
        self.gridLayout.addWidget(self.statusIcon, 0, 1, 1, 1)
        self.Separator1 = HorizontalSeparator(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Separator1.sizePolicy().hasHeightForWidth())
        self.Separator1.setSizePolicy(sizePolicy)
        self.Separator1.setObjectName("Separator1")
        self.gridLayout.addWidget(self.Separator1, 2, 1, 1, 2)
        self.title = SubtitleLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 2, 1, 1)
        self.setJavaWidget = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.setJavaWidget.sizePolicy().hasHeightForWidth()
        )
        self.setJavaWidget.setSizePolicy(sizePolicy)
        self.setJavaWidget.setMinimumSize(QSize(0, 120))
        self.setJavaWidget.setMaximumSize(QSize(16777215, 120))
        self.setJavaWidget.setObjectName("setJavaWidget")
        self.gridLayout_17 = QGridLayout(self.setJavaWidget)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.downloadJavaBtn = PrimaryPushButton(self.setJavaWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.downloadJavaBtn.sizePolicy().hasHeightForWidth()
        )
        self.downloadJavaBtn.setSizePolicy(sizePolicy)
        self.downloadJavaBtn.setMinimumSize(QSize(90, 0))
        self.downloadJavaBtn.setObjectName("downloadJavaBtn")
        self.gridLayout_17.addWidget(self.downloadJavaBtn, 2, 2, 1, 1)
        self.javaTitle = SubtitleLabel(self.setJavaWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.javaTitle.sizePolicy().hasHeightForWidth())
        self.javaTitle.setSizePolicy(sizePolicy)
        self.javaTitle.setObjectName("javaTitle")
        self.gridLayout_17.addWidget(self.javaTitle, 0, 0, 1, 1)
        self.selectJavaPrimaryPushBtn = PrimaryPushButton(self.setJavaWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.selectJavaPrimaryPushBtn.sizePolicy().hasHeightForWidth()
        )
        self.selectJavaPrimaryPushBtn.setSizePolicy(sizePolicy)
        self.selectJavaPrimaryPushBtn.setMinimumSize(QSize(90, 0))
        self.selectJavaPrimaryPushBtn.setObjectName("selectJavaPrimaryPushBtn")
        self.gridLayout_17.addWidget(self.selectJavaPrimaryPushBtn, 1, 2, 1, 1)
        self.autoDetectJavaBtn = PrimaryPushButton(self.setJavaWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.autoDetectJavaBtn.sizePolicy().hasHeightForWidth()
        )
        self.autoDetectJavaBtn.setSizePolicy(sizePolicy)
        self.autoDetectJavaBtn.setObjectName("autoDetectJavaBtn")
        self.gridLayout_17.addWidget(self.autoDetectJavaBtn, 1, 3, 1, 1)
        self.javaListBtn = PushButton(self.setJavaWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.javaListBtn.sizePolicy().hasHeightForWidth())
        self.javaListBtn.setSizePolicy(sizePolicy)
        self.javaListBtn.setMinimumSize(QSize(108, 0))
        self.javaListBtn.setMaximumSize(QSize(108, 16777215))
        self.javaListBtn.setObjectName("javaListBtn")
        self.gridLayout_17.addWidget(self.javaListBtn, 2, 3, 1, 1)
        self.shellArchivesValidateArgsJavaTextEdit = TextEdit(self.setJavaWidget)
        self.shellArchivesValidateArgsJavaTextEdit.setObjectName(
            "shellArchivesValidateArgsJavaTextEdit"
        )
        self.gridLayout_17.addWidget(
            self.shellArchivesValidateArgsJavaTextEdit, 1, 0, 2, 2
        )
        self.gridLayout.addWidget(self.setJavaWidget, 1, 1, 1, 2)
        self.setJVMArgWidget = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.setJVMArgWidget.sizePolicy().hasHeightForWidth()
        )
        self.setJVMArgWidget.setSizePolicy(sizePolicy)
        self.setJVMArgWidget.setMinimumSize(QSize(0, 171))
        self.setJVMArgWidget.setMaximumSize(QSize(16777215, 171))
        self.setJVMArgWidget.setObjectName("setJVMArgWidget")
        self.gridLayout_18 = QGridLayout(self.setJVMArgWidget)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.jvmArgPlainTextEdit = PlainTextEdit(self.setJVMArgWidget)
        self.jvmArgPlainTextEdit.setObjectName("jvmArgPlainTextEdit")
        self.gridLayout_18.addWidget(self.jvmArgPlainTextEdit, 1, 0, 1, 1)
        self.jvmArgTitle = SubtitleLabel(self.setJVMArgWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jvmArgTitle.sizePolicy().hasHeightForWidth())
        self.jvmArgTitle.setSizePolicy(sizePolicy)
        self.jvmArgTitle.setObjectName("jvmArgTitle")
        self.gridLayout_18.addWidget(self.jvmArgTitle, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.setJVMArgWidget, 7, 1, 1, 2)
        spacerItem = QSpacerItem(20, 625, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 8, 1)
        self.setMemWidget = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setMemWidget.sizePolicy().hasHeightForWidth())
        self.setMemWidget.setSizePolicy(sizePolicy)
        self.setMemWidget.setMinimumSize(QSize(0, 85))
        self.setMemWidget.setMaximumSize(QSize(16777215, 85))
        self.setMemWidget.setObjectName("setMemWidget")
        self.gridLayout_15 = QGridLayout(self.setMemWidget)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.minMemLineEdit = LineEdit(self.setMemWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.minMemLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.minMemLineEdit.setSizePolicy(sizePolicy)
        self.minMemLineEdit.setMinimumSize(QSize(0, 30))
        self.minMemLineEdit.setObjectName("minMemLineEdit")
        self.gridLayout_15.addWidget(self.minMemLineEdit, 1, 1, 1, 1)
        self.memTitle = SubtitleLabel(self.setMemWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.memTitle.sizePolicy().hasHeightForWidth())
        self.memTitle.setSizePolicy(sizePolicy)
        self.memTitle.setObjectName("memTitle")
        self.gridLayout_15.addWidget(self.memTitle, 0, 1, 1, 1)
        self.maxMemLineEdit = LineEdit(self.setMemWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.maxMemLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.maxMemLineEdit.setSizePolicy(sizePolicy)
        self.maxMemLineEdit.setMinimumSize(QSize(0, 30))
        self.maxMemLineEdit.setObjectName("maxMemLineEdit")
        self.gridLayout_15.addWidget(self.maxMemLineEdit, 1, 3, 1, 1)
        self.ToSymbol = SubtitleLabel(self.setMemWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToSymbol.sizePolicy().hasHeightForWidth())
        self.ToSymbol.setSizePolicy(sizePolicy)
        self.ToSymbol.setObjectName("ToSymbol")
        self.gridLayout_15.addWidget(self.ToSymbol, 1, 2, 1, 1)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem1, 1, 5, 1, 1)
        self.memUnitComboBox = ComboBox(self.setMemWidget)
        self.memUnitComboBox.setObjectName("memUnitComboBox")
        self.gridLayout_15.addWidget(self.memUnitComboBox, 1, 4, 1, 1)
        self.gridLayout.addWidget(self.setMemWidget, 3, 1, 1, 2)
        self.Separator2 = HorizontalSeparator(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Separator2.sizePolicy().hasHeightForWidth())
        self.Separator2.setSizePolicy(sizePolicy)
        self.Separator2.setObjectName("Separator2")
        self.gridLayout.addWidget(self.Separator2, 4, 1, 1, 2)
        self.setDeEncodingWidget = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.setDeEncodingWidget.sizePolicy().hasHeightForWidth()
        )
        self.setDeEncodingWidget.setSizePolicy(sizePolicy)
        self.setDeEncodingWidget.setMinimumSize(QSize(0, 122))
        self.setDeEncodingWidget.setMaximumSize(QSize(16777215, 122))
        self.setDeEncodingWidget.setObjectName("setDeEncodingWidget")
        self.gridLayout_16 = QGridLayout(self.setDeEncodingWidget)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.outputComboBox = ComboBox(self.setDeEncodingWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.outputComboBox.sizePolicy().hasHeightForWidth()
        )
        self.outputComboBox.setSizePolicy(sizePolicy)
        self.outputComboBox.setObjectName("outputComboBox")
        self.gridLayout_16.addWidget(self.outputComboBox, 2, 1, 1, 1)
        self.inputComboBox = ComboBox(self.setDeEncodingWidget)
        self.inputComboBox.setObjectName("inputComboBox")
        self.gridLayout_16.addWidget(self.inputComboBox, 3, 1, 1, 1)
        self.outputTitle = StrongBodyLabel(self.setDeEncodingWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputTitle.sizePolicy().hasHeightForWidth())
        self.outputTitle.setSizePolicy(sizePolicy)
        self.outputTitle.setObjectName("outputTitle")
        self.gridLayout_16.addWidget(self.outputTitle, 2, 0, 1, 1)
        self.setDeEncodingTitle = SubtitleLabel(self.setDeEncodingWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.setDeEncodingTitle.sizePolicy().hasHeightForWidth()
        )
        self.setDeEncodingTitle.setSizePolicy(sizePolicy)
        self.setDeEncodingTitle.setObjectName("setDeEncodingTitle")
        self.gridLayout_16.addWidget(self.setDeEncodingTitle, 0, 0, 1, 1)
        self.inputTitle = StrongBodyLabel(self.setDeEncodingWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputTitle.sizePolicy().hasHeightForWidth())
        self.inputTitle.setSizePolicy(sizePolicy)
        self.inputTitle.setObjectName("inputTitle")
        self.gridLayout_16.addWidget(self.inputTitle, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.setDeEncodingWidget, 5, 1, 1, 2)
        self.Separator3 = HorizontalSeparator(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Separator3.sizePolicy().hasHeightForWidth())
        self.Separator3.setSizePolicy(sizePolicy)
        self.Separator3.setObjectName("Separator3")
        self.gridLayout.addWidget(self.Separator3, 6, 1, 1, 2)
        self.title.setText("3. 设置参数")
        self.downloadJavaBtn.setText("下载Java")
        self.javaTitle.setText("Java:")
        self.selectJavaPrimaryPushBtn.setText("手动导入")
        self.autoDetectJavaBtn.setText("自动查找Java")
        self.javaListBtn.setText("Java列表")
        self.jvmArgPlainTextEdit.setPlaceholderText("可选，用一个空格分组")
        self.jvmArgTitle.setText("JVM参数：")
        self.memTitle.setText("内存:")
        self.ToSymbol.setText("~")
        self.outputTitle.setText("控制台输出编码（优先级高于全局设置）")
        self.setDeEncodingTitle.setText("编码设置：")
        self.inputTitle.setText("指令输入编码（优先级高于全局设置）")
        self.memUnitComboBox.addItems(["M", "G"])
        self.outputComboBox.addItems(
            [self.tr("跟随全局"), self.tr("UTF-8"), self.tr("GB18030"), self.tr("ANSI(推荐)")]
        )
        self.inputComboBox.addItems(
            [self.tr("跟随全局"), self.tr("UTF-8"), self.tr("GB18030"), self.tr("ANSI(推荐)")]
        )


class ImportFileFolderWidget(CardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("importFileFolderWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(0, 150))
        self.setMaximumSize(QSize(16777215, 150))
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QSpacerItem(265, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        self.statusIcon = PixmapLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusIcon.sizePolicy().hasHeightForWidth())
        self.statusIcon.setSizePolicy(sizePolicy)
        self.statusIcon.setMinimumSize(QSize(30, 30))
        self.statusIcon.setMaximumSize(QSize(30, 30))
        self.statusIcon.setObjectName("statusIcon")
        self.gridLayout.addWidget(self.statusIcon, 0, 1, 1, 1)
        self.title = SubtitleLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 2, 1, 2)
        self.importBtnWidget = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.importBtnWidget.sizePolicy().hasHeightForWidth()
        )
        self.importBtnWidget.setSizePolicy(sizePolicy)
        self.importBtnWidget.setObjectName("importBtnWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.importBtnWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.importFileBtn = PrimaryPushButton(self.importBtnWidget)
        self.importFileBtn.setMinimumSize(QSize(110, 32))
        self.importFileBtn.setMaximumSize(QSize(110, 32))
        self.importFileBtn.setObjectName("importFileBtn")
        self.horizontalLayout_2.addWidget(self.importFileBtn)
        self.ImportFolderBtn = PrimaryPushButton(self.importBtnWidget)
        self.ImportFolderBtn.setMinimumSize(QSize(110, 32))
        self.ImportFolderBtn.setMaximumSize(QSize(110, 32))
        self.ImportFolderBtn.setObjectName("ImportFolderBtn")
        self.horizontalLayout_2.addWidget(self.ImportFolderBtn)
        self.gridLayout.addWidget(self.importBtnWidget, 2, 1, 1, 2)
        self.statusText = BodyLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusText.sizePolicy().hasHeightForWidth())
        self.statusText.setSizePolicy(sizePolicy)
        self.statusText.setObjectName("statusText")
        self.gridLayout.addWidget(self.statusText, 1, 1, 1, 2)

        self.title.setText("1. 导入文件/文件夹")
        self.importFileBtn.setText("导入文件")
        self.ImportFolderBtn.setText("导入文件夹")
        # self.statusText.setText("[状态文本]")


class ImportSingleWidget(CardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("importSingleWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(0, 150))
        self.setMaximumSize(QSize(16777215, 150))
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.statusIcon = PixmapLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusIcon.sizePolicy().hasHeightForWidth())
        self.statusIcon.setSizePolicy(sizePolicy)
        self.statusIcon.setMinimumSize(QSize(30, 30))
        self.statusIcon.setMaximumSize(QSize(30, 30))
        self.statusIcon.setObjectName("statusIcon")
        self.gridLayout.addWidget(self.statusIcon, 0, 1, 1, 1)
        spacerItem = QSpacerItem(263, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 1)
        spacerItem1 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.title = SubtitleLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 2, 1, 2)
        self.importBtn = PrimaryPushButton(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importBtn.sizePolicy().hasHeightForWidth())
        self.importBtn.setSizePolicy(sizePolicy)
        self.importBtn.setMinimumSize(QSize(110, 32))
        self.importBtn.setMaximumSize(QSize(150, 32))
        self.importBtn.setObjectName("importBtn")
        self.gridLayout.addWidget(self.importBtn, 2, 1, 1, 2)
        self.statusText = BodyLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusText.sizePolicy().hasHeightForWidth())
        self.statusText.setSizePolicy(sizePolicy)
        self.statusText.setObjectName("statusText")
        self.gridLayout.addWidget(self.statusText, 1, 1, 1, 3)
        # self.title.setText("1. 选择MCSL 1主程序")
        # self.importBtn.setText("选择主程序")
        # self.statusText.setText("[状态文本]")


class ListWidget(CardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(0, 300))
        self.setMaximumSize(QSize(16777215, 300))
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.statusIcon = PixmapLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusIcon.sizePolicy().hasHeightForWidth())
        self.statusIcon.setSizePolicy(sizePolicy)
        self.statusIcon.setMinimumSize(QSize(30, 30))
        self.statusIcon.setMaximumSize(QSize(30, 30))
        self.statusIcon.setObjectName("statusIcon")
        self.gridLayout.addWidget(self.statusIcon, 0, 2, 1, 1)
        self.statusText = BodyLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusText.sizePolicy().hasHeightForWidth())
        self.statusText.setSizePolicy(sizePolicy)
        self.statusText.setObjectName("statusText")
        self.gridLayout.addWidget(self.statusText, 1, 2, 1, 2)
        spacerItem = QSpacerItem(20, 229, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 3, 1)
        self.title = SubtitleLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 3, 1, 1)
        self.mainListWidget = ListWidget(self)
        self.mainListWidget.setObjectName("mainListWidget")
        self.gridLayout.addWidget(self.mainListWidget, 2, 2, 1, 2)
        # self.statusText.setText("[状态文本]")
        # self.title.setText("2.选择核心")


class SaveWidget(CardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("saveWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(0, 135))
        self.setMaximumSize(QSize(16777215, 135))
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.saveServerNameLineEdit = LineEdit(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.saveServerNameLineEdit.sizePolicy().hasHeightForWidth()
        )
        self.saveServerNameLineEdit.setSizePolicy(sizePolicy)
        self.saveServerNameLineEdit.setMinimumSize(QSize(0, 30))
        self.saveServerNameLineEdit.setObjectName("saveServerNameLineEdit")
        self.gridLayout.addWidget(self.saveServerNameLineEdit, 1, 1, 1, 1)
        spacerItem = QSpacerItem(17, 101, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 3, 1)
        self.title = SubtitleLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setObjectName("saveTitle")
        self.gridLayout.addWidget(self.title, 0, 1, 1, 1)
        self.saveSaveServerBtn = PrimaryPushButton(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.saveSaveServerBtn.sizePolicy().hasHeightForWidth()
        )
        self.saveSaveServerBtn.setSizePolicy(sizePolicy)
        self.saveSaveServerBtn.setMinimumSize(QSize(130, 30))
        self.saveSaveServerBtn.setMaximumSize(QSize(16777215, 30))
        self.saveSaveServerBtn.setObjectName("saveSaveServerBtn")
        self.gridLayout.addWidget(self.saveSaveServerBtn, 2, 1, 1, 1)
        self.saveServerNameLineEdit.setPlaceholderText("设置服务器昵称，不能包含非法字符")
        self.saveSaveServerBtn.setText("导入！")
        # self.title.setText("4. 完成导入")

        self.saveServerNameLineEdit.textChanged.connect(
            lambda: self.saveSaveServerBtn.setEnabled(
                self.saveServerNameLineEdit.text() != ""
            )
        )