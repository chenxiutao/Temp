qss = '''QPalette{background:#EAF7FF;}*{outline:0px;color:#386487;}

QWidget[form="true"],QLabel[frameShape="1"]{
border:1px solid #C0DCF2;
border-radius:0px;
}

QWidget[form="bottom"]{
background:#DEF0FE;
}

QWidget[form="bottom"] .QFrame{
border:1px solid #386487;
}

QWidget[form="bottom"] QLabel,QWidget[form="title"] QLabel{
border-radius:0px;
color:#386487;
background:none;
border-style:none;
}

QWidget[form="title"],QWidget[nav="left"],QWidget[nav="top"] QAbstractButton{
border-style:none;
border-radius:0px;
padding:5px;
color:#386487;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QWidget[nav="top"] QAbstractButton:hover,QWidget[nav="top"] QAbstractButton:pressed,QWidget[nav="top"] QAbstractButton:checked{
border-style:solid;
border-width:0px 0px 2px 0px;
padding:4px 4px 2px 4px;
border-color:#00BB9E;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QWidget[nav="left"] QAbstractButton{
border-radius:0px;
color:#386487;
background:none;
border-style:none;
}

QWidget[nav="left"] QAbstractButton:hover{
color:#FFFFFF;
background-color:#00BB9E;
}

QWidget[nav="left"] QAbstractButton:checked,QWidget[nav="left"] QAbstractButton:pressed{
color:#386487;
border-style:solid;
border-width:0px 0px 0px 2px;
padding:4px 4px 4px 2px;
border-color:#00BB9E;
background-color:#EAF7FF;
}

QWidget[video="true"] QLabel{
color:#386487;
border:1px solid #C0DCF2;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QWidget[video="true"] QLabel:focus{
border:1px solid #00BB9E;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QDateEdit,QTimeEdit,QDateTimeEdit{
border:1px solid #C0DCF2;
border-radius:3px;
padding:2px;
background:none;
selection-background-color:#00BB9E;
selection-color:#FFFFFF;
}

QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{
border:1px solid #C0DCF2;
}

QLineEdit[echoMode="2"]{
lineedit-password-character:9679;
}

.QFrame{
border:1px solid #C0DCF2;
border-radius:3px;
}

.QGroupBox{
border:1px solid #C0DCF2;
border-radius:5px;
margin-top:3ex;
}

.QGroupBox::title{
subcontrol-origin:margin;
subcontrol-position: top center;
position:relative;
left:10px;
}

.QPushButton,.QToolButton{
border-style:none;
border:1px solid #C0DCF2;
color:#386487;
padding:5px;
min-height:15px;
border-radius:5px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QCheckBox {
	color: #000000;
	padding: 2px;
}
QCheckBox:disabled {
	color: #808086;
	padding: 2px;
}

QCheckBox:hover {
	border-radius:4px;
	border-style:solid;
	padding-left: 1px;
	padding-right: 1px;
	padding-bottom: 1px;
	padding-top: 1px;
	border-width:1px;
	border-color: transparent;
}
QCheckBox::indicator:checked {

	height: 10px;
	width: 10px;
	border-style:solid;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
	color: #000000;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
}
QCheckBox::indicator:unchecked {

	height: 10px;
	width: 10px;
	border-style:solid;
	border-width: 1px;
	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));
	color: #000000;
}

.QPushButton:hover,.QToolButton:hover{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

.QPushButton:pressed,.QToolButton:pressed{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

.QToolButton::menu-indicator{
image:None;
}

QToolButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{
border-radius:3px;
color:#386487;
padding:3px;
margin:0px;
background:none;
border-style:none;
}

QToolButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{
color:#FFFFFF;
margin:1px 1px 2px 1px;
background-color:rgba(51,127,209,230);
}

QPushButton#btnMenu_Close:hover{
color:#FFFFFF;
margin:1px 1px 2px 1px;
background-color:rgba(238,0,0,128);
}

/*QRadioButton::indicator{
width:15px;
height:15px;
}

QRadioButton::indicator::unchecked{
image:url(:./qss/lightblue/radiobutton_unchecked.png);
}

QRadioButton::indicator::unchecked:disabled{
image:url(:./qss/lightblue/radiobutton_unchecked_disable.png);
}

QRadioButton::indicator::checked{
image:url(:./qss/lightblue/radiobutton_checked.png);
}

QRadioButton::indicator::checked:disabled{
image:url(:./qss/lightblue/radiobutton_checked_disable.png);
}*/

QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
padding:0px -3px 0px 0px;
}

QCheckBox::indicator,QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
width:13px;
height:13px;
}

QCheckBox::indicator:unchecked,QGroupBox::indicator:unchecked,QTreeWidget::indicator:unchecked,QListWidget::indicator:unchecked{
image:url(:/qss/lightblue/checkbox_unchecked.png);
}

QCheckBox::indicator:unchecked:disabled,QGroupBox::indicator:unchecked:disabled,QTreeWidget::indicator:unchecked:disabled,QListWidget::indicator:disabled{
image:url(:/qss/lightblue/checkbox_unchecked_disable.png);
}

QCheckBox::indicator:checked,QGroupBox::indicator:checked,QTreeWidget::indicator:checked,QListWidget::indicator:checked{
image:url(:/qss/lightblue/checkbox_checked.png);
}

QCheckBox::indicator:checked:disabled,QGroupBox::indicator:checked:disabled,QTreeWidget::indicator:checked:disabled,QListWidget::indicator:checked:disabled{
image:url(:/qss/lightblue/checkbox_checked_disable.png);
}

QCheckBox::indicator:indeterminate,QGroupBox::indicator:indeterminate,QTreeWidget::indicator:indeterminate,QListWidget::indicator:indeterminate{
image:url(:/qss/lightblue/checkbox_parcial.png);
}

QCheckBox::indicator:indeterminate:disabled,QGroupBox::indicator:indeterminate:disabled,QTreeWidget::indicator:indeterminate:disabled,QListWidget::indicator:indeterminate:disabled{
image:url(:/qss/lightblue/checkbox_parcial_disable.png);
}

QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{
image:url(:/qss/lightblue/add_top.png);
width:10px;
height:10px;
padding:2px 5px 0px 0px;
}

QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{
image:url(:/qss/lightblue/add_bottom.png);
width:10px;
height:10px;
padding:0px 5px 2px 0px;
}

QTimeEdit::up-button:pressed,QDateEdit::up-button:pressed,QDateTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{
top:-2px;
}
  
QTimeEdit::down-button:pressed,QDateEdit::down-button:pressed,QDateTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{
bottom:-2px;
}

QDateEdit[calendarPopup="true"]::down-arrow,QTimeEdit[calendarPopup="true"]::down-arrow,QDateTimeEdit[calendarPopup="true"]::down-arrow{
image:url(:/qss/lightblue/add_bottom.png);
width:10px;
height:10px;
right:2px;
}

QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{
subcontrol-origin:padding;
subcontrol-position:top right;
width:15px;
border-left-width:0px;
border-left-style:solid;
border-top-right-radius:3px;
border-bottom-right-radius:3px;
border-left-color:#C0DCF2;
}

QMenuBar::item{
color:#386487;
background-color:#DEF0FE;
margin:0px;
padding:3px 10px;
}

QMenu,QMenuBar,QMenu:disabled,QMenuBar:disabled{
color:#386487;
background-color:#DEF0FE;
border:1px solid #C0DCF2;
margin:0px;
}

QMenu::item{
padding:3px 20px;
}

QMenu::indicator{
width:13px;
height:13px;
}

QMenu::item:selected,QMenuBar::item:selected{
color:#386487;
border:0px solid #C0DCF2;
background:#F2F9FF;
}

QMenu::separator{
height:1px;
background:#C0DCF2;
}

QProgressBar{
min-height:22px;
background:#DEF0FE;
border-radius:5px;
text-align:center;
border:1px solid #DEF0FE;
}

QProgressBar:chunk{
border-radius:5px;
background-color:#32CD32;
}

QSlider::groove:horizontal{
background:#DEF0FE;
height:8px;
border-radius:4px;
}

QSlider::add-page:horizontal{
background:#DEF0FE;
height:8px;
border-radius:4px;
}

QSlider::sub-page:horizontal{
background:#C0DCF2;
height:8px;
border-radius:4px;
}

QSlider::handle:horizontal{
width:13px;
margin-top:-3px;
margin-bottom:-3px;
border-radius:6px;
background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #EAF7FF,stop:0.8 #C0DCF2);
}

QSlider::groove:vertical{
width:8px;
border-radius:4px;
background:#DEF0FE;
}

QSlider::add-page:vertical{
width:8px;
border-radius:4px;
background:#DEF0FE;
}

QSlider::sub-page:vertical{
width:8px;
border-radius:4px;
background:#C0DCF2;
}

QSlider::handle:vertical{
height:14px;
margin-left:-3px;
margin-right:-3px;
border-radius:6px;
background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #EAF7FF,stop:0.8 #C0DCF2);
}

QScrollBar:horizontal{
background:#DEF0FE;
padding:0px;
border-radius:6px;
max-height:12px;
}

QScrollBar::handle:horizontal{
background:#C0DCF2;
min-width:50px;
border-radius:6px;
}

QScrollBar::handle:horizontal:hover{
background:#00BB9E;
}

QScrollBar::handle:horizontal:pressed{
background:#00BB9E;
}

QScrollBar::add-page:horizontal{
background:none;
}

QScrollBar::sub-page:horizontal{
background:none;
}

QScrollBar::add-line:horizontal{
background:none;
}

QScrollBar::sub-line:horizontal{
background:none;
}

QScrollBar:vertical{
background:#DEF0FE;
padding:0px;
border-radius:6px;
max-width:12px;
}

QScrollBar::handle:vertical{
background:#C0DCF2;
min-height:50px;
border-radius:6px;
}

QScrollBar::handle:vertical:hover{
background:#00BB9E;
}

QScrollBar::handle:vertical:pressed{
background:#00BB9E;
}

QScrollBar::add-page:vertical{
background:none;
}

QScrollBar::sub-page:vertical{
background:none;
}

QScrollBar::add-line:vertical{
background:none;
}

QScrollBar::sub-line:vertical{
background:none;
}

QScrollArea{
border:0px;
}

QTreeView,QListView,QTableView,QTabWidget::pane{
border:1px solid #C0DCF2;
selection-background-color:#F2F9FF;
selection-color:#386487;
alternate-background-color:#DAEFFF;
gridline-color:#C0DCF2;
}

QTreeView::branch:closed:has-children{
margin:4px;
border-image:url(:/qss/lightblue/branch_open.png);
}

QTreeView::branch:open:has-children{
margin:4px;
border-image:url(:/qss/lightblue/branch_close.png);
}

QTreeView,QListView,QTableView,QSplitter::handle,QTreeView::branch{
background:#EAF7FF;
}

QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{
color:#386487;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QTableView::item:hover,QListView::item:hover,QTreeView::item:hover,QHeaderView{
color:#386487;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QTableView::item,QListView::item,QTreeView::item{
padding:1px;
margin:0px;
}

QHeaderView::section,QTableCornerButton:section{
padding:3px;
margin:0px;
color:#386487;
border:1px solid #C0DCF2;
border-left-width:0px;
border-right-width:1px;
border-top-width:0px;
border-bottom-width:1px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QTabBar::tab{
border:1px solid #C0DCF2;
color:#386487;
margin:0px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QTabBar::tab:selected,QTabBar::tab:hover{
border-style:solid;
border-color:#00BB9E;
background:#EAF7FF;
}

QTabBar::tab:top,QTabBar::tab:bottom{
padding:3px 8px 3px 8px;
}

QTabBar::tab:left,QTabBar::tab:right{
padding:8px 3px 8px 3px;
}

QTabBar::tab:top:selected,QTabBar::tab:top:hover{
border-width:2px 0px 0px 0px;
}

QTabBar::tab:right:selected,QTabBar::tab:right:hover{
border-width:0px 0px 0px 2px;
}

QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
border-width:0px 0px 2px 0px;
}

QTabBar::tab:left:selected,QTabBar::tab:left:hover{
border-width:0px 2px 0px 0px;
}

QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{
border-left-width:1px;
border-left-color:#C0DCF2;
}

QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{
border-top-width:1px;
border-top-color:#C0DCF2;
}

QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{
border-right-width:1px;
border-right-color:#C0DCF2;
}

QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{
border-bottom-width:1px;
border-bottom-color:#C0DCF2;
}

QStatusBar::item{
border:0px solid #DEF0FE;
border-radius:3px;
}

QToolBox::tab,QGroupBox#gboxDevicePanel,QGroupBox#gboxDeviceTitle,QFrame#gboxDevicePanel,QFrame#gboxDeviceTitle{
padding:3px;
border-radius:5px;
color:#386487;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QToolTip{
border:0px solid #386487;
padding:1px;
color:#386487;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QToolBox::tab:selected{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QPrintPreviewDialog QToolButton{
border:0px solid #386487;
border-radius:0px;
margin:0px;
padding:3px;
background:none;
}

QColorDialog QPushButton,QFileDialog QPushButton{
min-width:80px;
}

QToolButton#qt_calendar_prevmonth{
icon-size:0px;
min-width:20px;
image:url(:/qss/lightblue/calendar_prevmonth.png);
}

QToolButton#qt_calendar_nextmonth{
icon-size:0px;
min-width:20px;
image:url(:/qss/lightblue/calendar_nextmonth.png);
}

QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{
border:0px solid #386487;
border-radius:3px;
margin:3px 3px 3px 3px;
padding:3px;
background:none;
}

QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{
border:1px solid #C0DCF2;
}

QCalendarWidget QSpinBox#qt_calendar_yearedit{
margin:2px;
}

QCalendarWidget QToolButton::menu-indicator{
image:None;
}

QCalendarWidget QTableView{
border-width:0px;
}

QCalendarWidget QWidget#qt_calendar_navigationbar{
border:1px solid #C0DCF2;
border-width:1px 1px 0px 1px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QTableView[model="true"]::item{
padding:0px;
margin:0px;
}

QTableView QLineEdit,QTableView QSpinBox,QTableView QDoubleSpinBox,QTableView QDateEdit,QTableView QTimeEdit,QTableView QDateTimeEdit{
border-width:0px;
border-radius:0px;
}

QTableView QLineEdit:focus,QTableView QSpinBox:focus,QTableView QDoubleSpinBox:focus,QTableView QDateEdit:focus,QTableView QTimeEdit:focus,QTableView QDateTimeEdit:focus{
border-width:0px;
border-radius:0px;
}

QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QDateEdit,QTimeEdit,QDateTimeEdit{
background:#EAF7FF;
}

QTabWidget::pane:top{top:-1px;}
QTabWidget::pane:bottom{bottom:-1px;}
QTabWidget::pane:left{right:-1px;}
QTabWidget::pane:right{left:-1px;}

*:disabled{
background:#EAF7FF;
border-color:#DEF0FE;
color:#C0DCF2;
}

/*TextColor:#386487*/
/*PanelColor:#EAF7FF*/
/*BorderColor:#C0DCF2*/
/*NormalColorStart:#DEF0FE*/
/*NormalColorEnd:#C0DEF6*/
/*DarkColorStart:#F2F9FF*/
/*DarkColorEnd:#DAEFFF*/
/*HighColor:#00BB9E*/'''