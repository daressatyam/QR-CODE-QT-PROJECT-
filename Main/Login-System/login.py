<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>LoginSystem</class>
 <widget class="QMainWindow" name="LoginSystem">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>750</width>
    <height>450</height>
   </rect>
  </property>
  <property name="maximumSize">
   <size>
    <width>750</width>
    <height>450</height>
   </size>
  </property>
  <property name="palette">
   <palette>
    <active>
     <colorrole role="WindowText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Base">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Window">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
    </active>
    <inactive>
     <colorrole role="WindowText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Base">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Window">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
    </inactive>
    <disabled>
     <colorrole role="WindowText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>120</red>
        <green>120</green>
        <blue>120</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Base">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Window">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
    </disabled>
   </palette>
  </property>
  <property name="windowTitle">
   <string>Login System 1.0</string>
  </property>
  <property name="windowIcon">
   <iconset resource="elements.qrc">
    <normaloff>:/icon.ico</normaloff>:/icon.ico</iconset>
  </property>
  <widget class="QWidget" name="centralWidget">
   <widget class="QFrame" name="frame">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>750</width>
      <height>450</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>750</width>
      <height>450</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>750</width>
      <height>450</height>
     </size>
    </property>
    <property name="baseSize">
     <size>
      <width>750</width>
      <height>450</height>
     </size>
    </property>
    <property name="autoFillBackground">
     <bool>false</bool>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <widget class="QStackedWidget" name="winStack">
     <property name="geometry">
      <rect>
       <x>0</x>
       <y>0</y>
       <width>751</width>
       <height>451</height>
      </rect>
     </property>
     <property name="currentIndex">
      <number>2</number>
     </property>
     <widget class="QWidget" name="Login">
      <widget class="QFrame" name="frame_2">
       <property name="geometry">
        <rect>
         <x>0</x>
         <y>0</y>
         <width>751</width>
         <height>451</height>
        </rect>
       </property>
       <property name="styleSheet">
        <string notr="true">background: #101010;</string>
       </property>
       <property name="frameShape">
        <enum>QFrame::StyledPanel</enum>
       </property>
       <property name="frameShadow">
        <enum>QFrame::Raised</enum>
       </property>
       <widget class="QLabel" name="label">
        <property name="geometry">
         <rect>
          <x>290</x>
          <y>22</y>
          <width>175</width>
          <height>41</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <family>Droid Sans</family>
          <pointsize>-1</pointsize>
         </font>
        </property>
        <property name="styleSheet">
         <string notr="true">text-align: center;
color: #393;
margin: 0 auto;
font-size: 35px;
font-family: 'Droid Sans';</string>
        </property>
        <property name="text">
         <string>Login</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="usernameBox">
        <property name="geometry">
         <rect>
          <x>50</x>
          <y>248</y>
          <width>201</width>
          <height>41</height>
         </rect>
        </property>
        <property name="palette">
         <palette>
          <active>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </active>
          <inactive>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </inactive>
          <disabled>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </disabled>
         </palette>
        </property>
        <property name="font">
         <font>
          <kerning>true</kerning>
         </font>
        </property>
        <property name="layoutDirection">
         <enum>Qt::LeftToRight</enum>
        </property>
        <property name="styleSheet">
         <string notr="true">padding-left: 20px;
padding-right: 20px;
border-radius: 20px;
background: #333;
color: #fefefe;</string>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="frame">
         <bool>false</bool>
        </property>
        <property name="cursorPosition">
         <number>0</number>
        </property>
        <property name="placeholderText">
         <string>Username</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="passwordBox">
        <property name="geometry">
         <rect>
          <x>50</x>
          <y>300</y>
          <width>201</width>
          <height>41</height>
         </rect>
        </property>
        <property name="palette">
         <palette>
          <active>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </active>
          <inactive>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </inactive>
          <disabled>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </disabled>
         </palette>
        </property>
        <property name="font">
         <font>
          <kerning>true</kerning>
         </font>
        </property>
        <property name="layoutDirection">
         <enum>Qt::LeftToRight</enum>
        </property>
        <property name="styleSheet">
         <string notr="true">padding-left: 20px;
padding-right: 20px;
border-radius: 20px;
background: #333;
color: #fefefe;</string>
        </property>
        <property name="inputMethodHints">
         <set>Qt::ImhNone</set>
        </property>
        <property name="inputMask">
         <string/>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="frame">
         <bool>false</bool>
        </property>
        <property name="cursorPosition">
         <number>0</number>
        </property>
        <property name="placeholderText">
         <string>Password</string>
        </property>
       </widget>
       <widget class="QPushButton" name="loginButton">
        <property name="geometry">
         <rect>
          <x>60</x>
          <y>354</y>
          <width>80</width>
          <height>21</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 5px;
Background: #393;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>SIGN IN</string>
        </property>
       </widget>
       <widget class="QPushButton" name="regButton">
        <property name="geometry">
         <rect>
          <x>160</x>
          <y>354</y>
          <width>80</width>
          <height>21</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 5px;
Background: #933;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>SIGN UP</string>
        </property>
       </widget>
       <widget class="QLabel" name="loginLabel">
        <property name="geometry">
         <rect>
          <x>60</x>
          <y>222</y>
          <width>267</width>
          <height>16</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #fefefe;</string>
        </property>
        <property name="text">
         <string/>
        </property>
       </widget>
       <widget class="QLabel" name="label_7">
        <property name="geometry">
         <rect>
          <x>88</x>
          <y>80</y>
          <width>128</width>
          <height>128</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">border-radius: 64px;
background-image: url(:/user.png);</string>
        </property>
        <property name="text">
         <string/>
        </property>
       </widget>
      </widget>
     </widget>
     <widget class="QWidget" name="page_2">
      <widget class="QFrame" name="frame_3">
       <property name="geometry">
        <rect>
         <x>0</x>
         <y>0</y>
         <width>751</width>
         <height>451</height>
        </rect>
       </property>
       <property name="styleSheet">
        <string notr="true">background: #101010;</string>
       </property>
       <property name="frameShape">
        <enum>QFrame::StyledPanel</enum>
       </property>
       <property name="frameShadow">
        <enum>QFrame::Raised</enum>
       </property>
       <widget class="QLabel" name="label_2">
        <property name="geometry">
         <rect>
          <x>258</x>
          <y>24</y>
          <width>223</width>
          <height>41</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <family>Droid Sans</family>
          <pointsize>-1</pointsize>
         </font>
        </property>
        <property name="styleSheet">
         <string notr="true">text-align: center;
color: #393;
margin: 0 auto;
font-size: 35px;
font-family: 'Droid Sans';</string>
        </property>
        <property name="text">
         <string>Register</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="uBox">
        <property name="geometry">
         <rect>
          <x>70</x>
          <y>160</y>
          <width>201</width>
          <height>41</height>
         </rect>
        </property>
        <property name="palette">
         <palette>
          <active>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </active>
          <inactive>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </inactive>
          <disabled>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </disabled>
         </palette>
        </property>
        <property name="font">
         <font>
          <kerning>true</kerning>
         </font>
        </property>
        <property name="layoutDirection">
         <enum>Qt::LeftToRight</enum>
        </property>
        <property name="styleSheet">
         <string notr="true">padding-left: 20px;
padding-right: 20px;
border-radius: 20px;
background: #333;
color: #fefefe;</string>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="frame">
         <bool>false</bool>
        </property>
        <property name="cursorPosition">
         <number>0</number>
        </property>
        <property name="placeholderText">
         <string>Username</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="pBox">
        <property name="geometry">
         <rect>
          <x>70</x>
          <y>220</y>
          <width>201</width>
          <height>41</height>
         </rect>
        </property>
        <property name="palette">
         <palette>
          <active>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </active>
          <inactive>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </inactive>
          <disabled>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </disabled>
         </palette>
        </property>
        <property name="font">
         <font>
          <kerning>true</kerning>
         </font>
        </property>
        <property name="layoutDirection">
         <enum>Qt::LeftToRight</enum>
        </property>
        <property name="styleSheet">
         <string notr="true">padding-left: 20px;
padding-right: 20px;
border-radius: 20px;
background: #333;
color: #fefefe;</string>
        </property>
        <property name="inputMethodHints">
         <set>Qt::ImhNone</set>
        </property>
        <property name="inputMask">
         <string/>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="frame">
         <bool>false</bool>
        </property>
        <property name="cursorPosition">
         <number>0</number>
        </property>
        <property name="placeholderText">
         <string>Password</string>
        </property>
       </widget>
       <widget class="QPushButton" name="completeRegButton">
        <property name="geometry">
         <rect>
          <x>540</x>
          <y>400</y>
          <width>171</width>
          <height>21</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 5px;
Background: #393;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>COMPLETE REGISTRATION</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="eBox">
        <property name="geometry">
         <rect>
          <x>70</x>
          <y>280</y>
          <width>201</width>
          <height>41</height>
         </rect>
        </property>
        <property name="palette">
         <palette>
          <active>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </active>
          <inactive>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </inactive>
          <disabled>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </disabled>
         </palette>
        </property>
        <property name="font">
         <font>
          <kerning>true</kerning>
         </font>
        </property>
        <property name="layoutDirection">
         <enum>Qt::LeftToRight</enum>
        </property>
        <property name="styleSheet">
         <string notr="true">padding-left: 20px;
padding-right: 20px;
border-radius: 20px;
background: #333;
color: #fefefe;</string>
        </property>
        <property name="inputMethodHints">
         <set>Qt::ImhNone</set>
        </property>
        <property name="inputMask">
         <string/>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="frame">
         <bool>false</bool>
        </property>
        <property name="cursorPosition">
         <number>0</number>
        </property>
        <property name="placeholderText">
         <string>E-mail</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="fBox">
        <property name="geometry">
         <rect>
          <x>490</x>
          <y>160</y>
          <width>201</width>
          <height>41</height>
         </rect>
        </property>
        <property name="palette">
         <palette>
          <active>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </active>
          <inactive>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </inactive>
          <disabled>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </disabled>
         </palette>
        </property>
        <property name="font">
         <font>
          <kerning>true</kerning>
         </font>
        </property>
        <property name="layoutDirection">
         <enum>Qt::LeftToRight</enum>
        </property>
        <property name="styleSheet">
         <string notr="true">padding-left: 20px;
padding-right: 20px;
border-radius: 20px;
background: #333;
color: #fefefe;</string>
        </property>
        <property name="inputMethodHints">
         <set>Qt::ImhNone</set>
        </property>
        <property name="inputMask">
         <string/>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="frame">
         <bool>false</bool>
        </property>
        <property name="cursorPosition">
         <number>0</number>
        </property>
        <property name="placeholderText">
         <string>First Name</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="mBox">
        <property name="geometry">
         <rect>
          <x>490</x>
          <y>220</y>
          <width>201</width>
          <height>41</height>
         </rect>
        </property>
        <property name="palette">
         <palette>
          <active>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </active>
          <inactive>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </inactive>
          <disabled>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </disabled>
         </palette>
        </property>
        <property name="font">
         <font>
          <kerning>true</kerning>
         </font>
        </property>
        <property name="layoutDirection">
         <enum>Qt::LeftToRight</enum>
        </property>
        <property name="styleSheet">
         <string notr="true">padding-left: 20px;
padding-right: 20px;
border-radius: 20px;
background: #333;
color: #fefefe;</string>
        </property>
        <property name="inputMethodHints">
         <set>Qt::ImhNone</set>
        </property>
        <property name="inputMask">
         <string/>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="frame">
         <bool>false</bool>
        </property>
        <property name="cursorPosition">
         <number>0</number>
        </property>
        <property name="placeholderText">
         <string>Middle Name</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="lBox">
        <property name="geometry">
         <rect>
          <x>490</x>
          <y>280</y>
          <width>201</width>
          <height>41</height>
         </rect>
        </property>
        <property name="palette">
         <palette>
          <active>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </active>
          <inactive>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </inactive>
          <disabled>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </disabled>
         </palette>
        </property>
        <property name="font">
         <font>
          <kerning>true</kerning>
         </font>
        </property>
        <property name="layoutDirection">
         <enum>Qt::LeftToRight</enum>
        </property>
        <property name="styleSheet">
         <string notr="true">padding-left: 20px;
padding-right: 20px;
border-radius: 20px;
background: #333;
color: #fefefe;</string>
        </property>
        <property name="inputMethodHints">
         <set>Qt::ImhNone</set>
        </property>
        <property name="inputMask">
         <string/>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="frame">
         <bool>false</bool>
        </property>
        <property name="cursorPosition">
         <number>0</number>
        </property>
        <property name="placeholderText">
         <string>Last Name</string>
        </property>
       </widget>
       <widget class="QPushButton" name="backButton">
        <property name="geometry">
         <rect>
          <x>40</x>
          <y>400</y>
          <width>171</width>
          <height>21</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 5px;
Background: #933;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>BACK TO LOGIN PAGE</string>
        </property>
       </widget>
       <widget class="QLabel" name="regLabel">
        <property name="geometry">
         <rect>
          <x>60</x>
          <y>110</y>
          <width>601</width>
          <height>16</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #fefefe;</string>
        </property>
        <property name="text">
         <string>Please fill the form correctly.</string>
        </property>
       </widget>
       <widget class="QLabel" name="rpLabel">
        <property name="geometry">
         <rect>
          <x>316</x>
          <y>148</y>
          <width>128</width>
          <height>128</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #fefefe;</string>
        </property>
        <property name="text">
         <string>&lt;img src=&quot;:user.png&quot; /&gt;</string>
        </property>
       </widget>
       <widget class="QPushButton" name="uplButton">
        <property name="geometry">
         <rect>
          <x>298</x>
          <y>294</y>
          <width>171</width>
          <height>21</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 5px;
Background: #339;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>UPLOAD PICTURE</string>
        </property>
       </widget>
      </widget>
     </widget>
     <widget class="QWidget" name="page">
      <widget class="QFrame" name="frame_4">
       <property name="geometry">
        <rect>
         <x>0</x>
         <y>0</y>
         <width>751</width>
         <height>451</height>
        </rect>
       </property>
       <property name="styleSheet">
        <string notr="true">background: #101010;</string>
       </property>
       <property name="frameShape">
        <enum>QFrame::StyledPanel</enum>
       </property>
       <property name="frameShadow">
        <enum>QFrame::Raised</enum>
       </property>
       <widget class="QLabel" name="loggedUserHeader">
        <property name="geometry">
         <rect>
          <x>248</x>
          <y>16</y>
          <width>245</width>
          <height>41</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <family>Droid Sans</family>
          <pointsize>-1</pointsize>
         </font>
        </property>
        <property name="styleSheet">
         <string notr="true">text-align: center;
color: #393;
margin: 0 auto;
font-size: 35px;
font-family: 'Droid Sans';</string>
        </property>
        <property name="text">
         <string>Logged In</string>
        </property>
       </widget>
       <widget class="QPushButton" name="logoutButton">
        <property name="geometry">
         <rect>
          <x>570</x>
          <y>150</y>
          <width>151</width>
          <height>21</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 5px;
Background: #933;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>SIGN OUT</string>
        </property>
       </widget>
       <widget class="QLabel" name="label_3">
        <property name="geometry">
         <rect>
          <x>54</x>
          <y>248</y>
          <width>47</width>
          <height>13</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #c33;
font-weight: bold;</string>
        </property>
        <property name="text">
         <string>Name:</string>
        </property>
       </widget>
       <widget class="QLabel" name="label_4">
        <property name="geometry">
         <rect>
          <x>54</x>
          <y>278</y>
          <width>47</width>
          <height>13</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #c33;
font-weight: bold;</string>
        </property>
        <property name="text">
         <string>Rank:</string>
        </property>
       </widget>
       <widget class="QLabel" name="nameLabel">
        <property name="geometry">
         <rect>
          <x>124</x>
          <y>248</y>
          <width>241</width>
          <height>16</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #fefefe;</string>
        </property>
        <property name="text">
         <string/>
        </property>
       </widget>
       <widget class="QLabel" name="rankLabel">
        <property name="geometry">
         <rect>
          <x>124</x>
          <y>278</y>
          <width>201</width>
          <height>16</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #fefefe;</string>
        </property>
        <property name="text">
         <string/>
        </property>
       </widget>
       <widget class="QPushButton" name="editButton">
        <property name="geometry">
         <rect>
          <x>570</x>
          <y>180</y>
          <width>151</width>
          <height>21</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 5px;
Background: #393;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>EDIT MY PROFILE</string>
        </property>
       </widget>
       <widget class="QPushButton" name="delButton">
        <property name="geometry">
         <rect>
          <x>570</x>
          <y>212</y>
          <width>151</width>
          <height>21</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 5px;
Background: #aaa;
Color: #101010;</string>
        </property>
        <property name="text">
         <string>DELETE MY ACCOUNT</string>
        </property>
       </widget>
       <widget class="QLabel" name="label_6">
        <property name="geometry">
         <rect>
          <x>48</x>
          <y>306</y>
          <width>47</width>
          <height>13</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #c33;
font-weight: bold;</string>
        </property>
        <property name="text">
         <string>E-mail:</string>
        </property>
       </widget>
       <widget class="QLabel" name="emailLabel">
        <property name="geometry">
         <rect>
          <x>124</x>
          <y>306</y>
          <width>201</width>
          <height>16</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #fefefe;</string>
        </property>
        <property name="text">
         <string/>
        </property>
       </widget>
       <widget class="QFrame" name="frame_6">
        <property name="geometry">
         <rect>
          <x>120</x>
          <y>92</y>
          <width>128</width>
          <height>128</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true"/>
        </property>
        <property name="frameShape">
         <enum>QFrame::StyledPanel</enum>
        </property>
        <property name="frameShadow">
         <enum>QFrame::Raised</enum>
        </property>
        <widget class="QLabel" name="loggedPic">
         <property name="geometry">
          <rect>
           <x>0</x>
           <y>0</y>
           <width>128</width>
           <height>128</height>
          </rect>
         </property>
         <property name="styleSheet">
          <string notr="true"/>
         </property>
         <property name="text">
          <string>&lt;img src=&quot;:user.png&quot; /&gt;</string>
         </property>
        </widget>
       </widget>
       <widget class="QPushButton" name="adminButton">
        <property name="geometry">
         <rect>
          <x>570</x>
          <y>118</y>
          <width>151</width>
          <height>21</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 5px;
Background: #339;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>ADMIN PANEL</string>
        </property>
       </widget>
       <zorder>frame_6</zorder>
       <zorder>loggedUserHeader</zorder>
       <zorder>logoutButton</zorder>
       <zorder>label_3</zorder>
       <zorder>label_4</zorder>
       <zorder>nameLabel</zorder>
       <zorder>rankLabel</zorder>
       <zorder>editButton</zorder>
       <zorder>delButton</zorder>
       <zorder>label_6</zorder>
       <zorder>emailLabel</zorder>
       <zorder>adminButton</zorder>
      </widget>
     </widget>
     <widget class="QWidget" name="page_3">
      <widget class="QFrame" name="frame_5">
       <property name="geometry">
        <rect>
         <x>0</x>
         <y>0</y>
         <width>751</width>
         <height>451</height>
        </rect>
       </property>
       <property name="styleSheet">
        <string notr="true">background: #101010;</string>
       </property>
       <property name="frameShape">
        <enum>QFrame::StyledPanel</enum>
       </property>
       <property name="frameShadow">
        <enum>QFrame::Raised</enum>
       </property>
       <widget class="QLabel" name="label_5">
        <property name="geometry">
         <rect>
          <x>238</x>
          <y>20</y>
          <width>273</width>
          <height>41</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <family>Droid Sans</family>
          <pointsize>-1</pointsize>
         </font>
        </property>
        <property name="styleSheet">
         <string notr="true">text-align: center;
color: #393;
margin: 0 auto;
font-size: 35px;
font-family: 'Droid Sans';</string>
        </property>
        <property name="text">
         <string>Edit Profile</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="uBox_2">
        <property name="geometry">
         <rect>
          <x>70</x>
          <y>160</y>
          <width>201</width>
          <height>41</height>
         </rect>
        </property>
        <property name="palette">
         <palette>
          <active>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </active>
          <inactive>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </inactive>
          <disabled>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </disabled>
         </palette>
        </property>
        <property name="font">
         <font>
          <kerning>true</kerning>
         </font>
        </property>
        <property name="layoutDirection">
         <enum>Qt::LeftToRight</enum>
        </property>
        <property name="styleSheet">
         <string notr="true">padding-left: 20px;
padding-right: 20px;
border-radius: 20px;
background: #333;
color: #fefefe;</string>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="frame">
         <bool>false</bool>
        </property>
        <property name="cursorPosition">
         <number>0</number>
        </property>
        <property name="placeholderText">
         <string>Username</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="pBox_2">
        <property name="geometry">
         <rect>
          <x>70</x>
          <y>220</y>
          <width>201</width>
          <height>41</height>
         </rect>
        </property>
        <property name="palette">
         <palette>
          <active>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </active>
          <inactive>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </inactive>
          <disabled>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </disabled>
         </palette>
        </property>
        <property name="font">
         <font>
          <kerning>true</kerning>
         </font>
        </property>
        <property name="layoutDirection">
         <enum>Qt::LeftToRight</enum>
        </property>
        <property name="styleSheet">
         <string notr="true">padding-left: 20px;
padding-right: 20px;
border-radius: 20px;
background: #333;
color: #fefefe;</string>
        </property>
        <property name="inputMethodHints">
         <set>Qt::ImhNone</set>
        </property>
        <property name="inputMask">
         <string/>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="frame">
         <bool>false</bool>
        </property>
        <property name="cursorPosition">
         <number>0</number>
        </property>
        <property name="placeholderText">
         <string>Password</string>
        </property>
       </widget>
       <widget class="QPushButton" name="editedButton">
        <property name="geometry">
         <rect>
          <x>540</x>
          <y>400</y>
          <width>171</width>
          <height>21</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 5px;
Background: #393;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>SUBMIT CHANGES</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="eBox_2">
        <property name="geometry">
         <rect>
          <x>70</x>
          <y>280</y>
          <width>201</width>
          <height>41</height>
         </rect>
        </property>
        <property name="palette">
         <palette>
          <active>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </active>
          <inactive>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </inactive>
          <disabled>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </disabled>
         </palette>
        </property>
        <property name="font">
         <font>
          <kerning>true</kerning>
         </font>
        </property>
        <property name="layoutDirection">
         <enum>Qt::LeftToRight</enum>
        </property>
        <property name="styleSheet">
         <string notr="true">padding-left: 20px;
padding-right: 20px;
border-radius: 20px;
background: #333;
color: #fefefe;</string>
        </property>
        <property name="inputMethodHints">
         <set>Qt::ImhNone</set>
        </property>
        <property name="inputMask">
         <string/>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="frame">
         <bool>false</bool>
        </property>
        <property name="cursorPosition">
         <number>0</number>
        </property>
        <property name="placeholderText">
         <string>E-mail</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="fBox_2">
        <property name="geometry">
         <rect>
          <x>490</x>
          <y>160</y>
          <width>201</width>
          <height>41</height>
         </rect>
        </property>
        <property name="palette">
         <palette>
          <active>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </active>
          <inactive>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </inactive>
          <disabled>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </disabled>
         </palette>
        </property>
        <property name="font">
         <font>
          <kerning>true</kerning>
         </font>
        </property>
        <property name="layoutDirection">
         <enum>Qt::LeftToRight</enum>
        </property>
        <property name="styleSheet">
         <string notr="true">padding-left: 20px;
padding-right: 20px;
border-radius: 20px;
background: #333;
color: #fefefe;</string>
        </property>
        <property name="inputMethodHints">
         <set>Qt::ImhNone</set>
        </property>
        <property name="inputMask">
         <string/>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="frame">
         <bool>false</bool>
        </property>
        <property name="cursorPosition">
         <number>0</number>
        </property>
        <property name="placeholderText">
         <string>First Name</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="mBox_2">
        <property name="geometry">
         <rect>
          <x>490</x>
          <y>220</y>
          <width>201</width>
          <height>41</height>
         </rect>
        </property>
        <property name="palette">
         <palette>
          <active>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </active>
          <inactive>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </inactive>
          <disabled>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </disabled>
         </palette>
        </property>
        <property name="font">
         <font>
          <kerning>true</kerning>
         </font>
        </property>
        <property name="layoutDirection">
         <enum>Qt::LeftToRight</enum>
        </property>
        <property name="styleSheet">
         <string notr="true">padding-left: 20px;
padding-right: 20px;
border-radius: 20px;
background: #333;
color: #fefefe;</string>
        </property>
        <property name="inputMethodHints">
         <set>Qt::ImhNone</set>
        </property>
        <property name="inputMask">
         <string/>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="frame">
         <bool>false</bool>
        </property>
        <property name="cursorPosition">
         <number>0</number>
        </property>
        <property name="placeholderText">
         <string>Middle Name</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="lBox_2">
        <property name="geometry">
         <rect>
          <x>490</x>
          <y>280</y>
          <width>201</width>
          <height>41</height>
         </rect>
        </property>
        <property name="palette">
         <palette>
          <active>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </active>
          <inactive>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </inactive>
          <disabled>
           <colorrole role="WindowText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Button">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Text">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="ButtonText">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Base">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="Window">
            <brush brushstyle="SolidPattern">
             <color alpha="255">
              <red>51</red>
              <green>51</green>
              <blue>51</blue>
             </color>
            </brush>
           </colorrole>
           <colorrole role="PlaceholderText">
            <brush brushstyle="NoBrush">
             <color alpha="128">
              <red>254</red>
              <green>254</green>
              <blue>254</blue>
             </color>
            </brush>
           </colorrole>
          </disabled>
         </palette>
        </property>
        <property name="font">
         <font>
          <kerning>true</kerning>
         </font>
        </property>
        <property name="layoutDirection">
         <enum>Qt::LeftToRight</enum>
        </property>
        <property name="styleSheet">
         <string notr="true">padding-left: 20px;
padding-right: 20px;
border-radius: 20px;
background: #333;
color: #fefefe;</string>
        </property>
        <property name="inputMethodHints">
         <set>Qt::ImhNone</set>
        </property>
        <property name="inputMask">
         <string/>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="frame">
         <bool>false</bool>
        </property>
        <property name="cursorPosition">
         <number>0</number>
        </property>
        <property name="placeholderText">
         <string>Last Name</string>
        </property>
       </widget>
       <widget class="QPushButton" name="backButton_2">
        <property name="geometry">
         <rect>
          <x>40</x>
          <y>400</y>
          <width>171</width>
          <height>21</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 5px;
Background: #933;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>BACK TO MY PAGE</string>
        </property>
       </widget>
       <widget class="QLabel" name="regLabel_2">
        <property name="geometry">
         <rect>
          <x>60</x>
          <y>110</y>
          <width>601</width>
          <height>16</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #fefefe;</string>
        </property>
        <property name="text">
         <string>Edit your details below. (avatar may not change until app relaunch)</string>
        </property>
       </widget>
       <widget class="QPushButton" name="uplButton_2">
        <property name="geometry">
         <rect>
          <x>294</x>
          <y>292</y>
          <width>171</width>
          <height>21</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 5px;
Background: #339;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>CHANGE PICTURE</string>
        </property>
       </widget>
       <widget class="QLabel" name="rpLabel_2">
        <property name="geometry">
         <rect>
          <x>312</x>
          <y>146</y>
          <width>128</width>
          <height>128</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #fefefe;</string>
        </property>
        <property name="text">
         <string>&lt;img src=&quot;:user.png&quot; /&gt;</string>
        </property>
       </widget>
       <zorder>label_5</zorder>
       <zorder>uBox_2</zorder>
       <zorder>pBox_2</zorder>
       <zorder>eBox_2</zorder>
       <zorder>fBox_2</zorder>
       <zorder>mBox_2</zorder>
       <zorder>lBox_2</zorder>
       <zorder>backButton_2</zorder>
       <zorder>regLabel_2</zorder>
       <zorder>editedButton</zorder>
       <zorder>uplButton_2</zorder>
       <zorder>rpLabel_2</zorder>
      </widget>
     </widget>
     <widget class="QWidget" name="page_4">
      <widget class="QFrame" name="frame_7">
       <property name="geometry">
        <rect>
         <x>0</x>
         <y>0</y>
         <width>751</width>
         <height>451</height>
        </rect>
       </property>
       <property name="styleSheet">
        <string notr="true">background: #101010;</string>
       </property>
       <property name="frameShape">
        <enum>QFrame::StyledPanel</enum>
       </property>
       <property name="frameShadow">
        <enum>QFrame::Raised</enum>
       </property>
       <widget class="QLabel" name="label_8">
        <property name="geometry">
         <rect>
          <x>234</x>
          <y>20</y>
          <width>291</width>
          <height>41</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <family>Droid Sans</family>
          <pointsize>-1</pointsize>
         </font>
        </property>
        <property name="styleSheet">
         <string notr="true">text-align: center;
color: #393;
margin: 0 auto;
font-size: 35px;
font-family: 'Droid Sans';</string>
        </property>
        <property name="text">
         <string>Admin Panel</string>
        </property>
       </widget>
       <widget class="QPushButton" name="editedButton_2">
        <property name="geometry">
         <rect>
          <x>558</x>
          <y>410</y>
          <width>171</width>
          <height>21</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 5px;
Background: #393;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>SAVE CHANGES</string>
        </property>
       </widget>
       <widget class="QPushButton" name="delUButton">
        <property name="geometry">
         <rect>
          <x>22</x>
          <y>410</y>
          <width>171</width>
          <height>21</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 5px;
Background: #a11;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>DELETE ALL USERS</string>
        </property>
       </widget>
       <widget class="QStackedWidget" name="stackedWidget">
        <property name="geometry">
         <rect>
          <x>182</x>
          <y>122</y>
          <width>535</width>
          <height>251</height>
         </rect>
        </property>
        <property name="currentIndex">
         <number>0</number>
        </property>
        <widget class="QWidget" name="page_5">
         <widget class="QFrame" name="frame_8">
          <property name="geometry">
           <rect>
            <x>0</x>
            <y>0</y>
            <width>535</width>
            <height>303</height>
           </rect>
          </property>
          <property name="styleSheet">
           <string notr="true">background: #fefefe;</string>
          </property>
          <property name="frameShape">
           <enum>QFrame::StyledPanel</enum>
          </property>
          <property name="frameShadow">
           <enum>QFrame::Raised</enum>
          </property>
          <widget class="QTableView" name="tableView">
           <property name="geometry">
            <rect>
             <x>0</x>
             <y>0</y>
             <width>535</width>
             <height>305</height>
            </rect>
           </property>
          </widget>
         </widget>
        </widget>
        <widget class="QWidget" name="page_6">
         <widget class="QFrame" name="frame_9">
          <property name="geometry">
           <rect>
            <x>0</x>
            <y>0</y>
            <width>535</width>
            <height>303</height>
           </rect>
          </property>
          <property name="styleSheet">
           <string notr="true">background: #fefefe;</string>
          </property>
          <property name="frameShape">
           <enum>QFrame::StyledPanel</enum>
          </property>
          <property name="frameShadow">
           <enum>QFrame::Raised</enum>
          </property>
          <widget class="QTableView" name="tableView_2">
           <property name="geometry">
            <rect>
             <x>0</x>
             <y>-2</y>
             <width>535</width>
             <height>305</height>
            </rect>
           </property>
          </widget>
         </widget>
        </widget>
       </widget>
       <widget class="QPushButton" name="userBrowse">
        <property name="geometry">
         <rect>
          <x>18</x>
          <y>166</y>
          <width>155</width>
          <height>27</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 0;
Background: #393;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>ALL USERS</string>
        </property>
       </widget>
       <widget class="QPushButton" name="backButton_5">
        <property name="geometry">
         <rect>
          <x>380</x>
          <y>410</y>
          <width>171</width>
          <height>21</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 5px;
Background: #339;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>ROLLBACK ALL CHANGES</string>
        </property>
       </widget>
       <widget class="QPushButton" name="pageButton">
        <property name="geometry">
         <rect>
          <x>18</x>
          <y>246</y>
          <width>155</width>
          <height>27</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 0;
Background: #393;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>GOTO MY PAGE</string>
        </property>
       </widget>
       <widget class="QPushButton" name="adminBrowse">
        <property name="geometry">
         <rect>
          <x>18</x>
          <y>206</y>
          <width>155</width>
          <height>27</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 0;
Background: #393;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>ALL ADMINS</string>
        </property>
       </widget>
       <widget class="QPushButton" name="delAButton">
        <property name="geometry">
         <rect>
          <x>202</x>
          <y>410</y>
          <width>171</width>
          <height>21</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">Padding: 1px;
Border-radius: 5px;
Background: #a11;
Color: #fefefe;</string>
        </property>
        <property name="text">
         <string>DELETE ALL ADMINS</string>
        </property>
       </widget>
       <widget class="QLabel" name="adminLabel">
        <property name="geometry">
         <rect>
          <x>50</x>
          <y>386</y>
          <width>649</width>
          <height>16</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #fefefe;</string>
        </property>
        <property name="text">
         <string>There are no auto backups! Be sure of any alterations you make.</string>
        </property>
       </widget>
       <widget class="QLabel" name="headLabel">
        <property name="geometry">
         <rect>
          <x>190</x>
          <y>100</y>
          <width>479</width>
          <height>16</height>
         </rect>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #fefefe;</string>
        </property>
        <property name="text">
         <string/>
        </property>
       </widget>
      </widget>
     </widget>
    </widget>
   </widget>
  </widget>
 </widget>
 <layoutdefault spacing="6" margin="11"/>
 <resources>
  <include location="elements.qrc"/>
 </resources>
 <connections/>
</ui>
