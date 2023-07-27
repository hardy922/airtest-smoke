# -*- coding: utf-8 -*-
# @Author: Hardy
# @Time: 2023/2/9 14:36
# @File: elements.py
# @Software: PyCharm


class LightPlayLogin(object):
    # 环境选择
    ENV_SELECTOR = "com.demo:id/drop_down"
    # 咪咕正式
    ENV_MI_GU = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[1]"
    # 咪咕灰度
    ENV_MI_GU_BETA = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[2]"
    # 网易正式
    ENV_WANG_YI = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[3]"
    # 网易灰度
    ENV_WANG_YI_BETA = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[4]"
    # B站正式
    ENV_B = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[5]"
    # 乐播正式
    ENV_LEBO = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[6]"
    # B站Beta
    ENV_B_BETA = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[7]"
    # 快手正式
    ENV_KUAI_SHOU = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[8]"
    # 快手beta
    ENV_KUAI_SHOU_BETA = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[9]"
    # 斗鱼
    ENV_DOUYU = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[10]"
    # area地址端口
    AREA_PORT = "com.demo:id/ipAreaEt"
    # 上报地址
    REPORT = "com.demo:id/et_reportUrl"
    # vmid
    VM_ID = "com.demo:id/vmidEt"
    # biz
    BIZ = "com.demo:id/biz_et"
    # 尝试输入指定区域
    AREA_TYPE = "com.demo:id/areaTypeEt"
    # 强制输入指定区域
    DEBUG_AREA = "com.demo:id/et_debugArea"
    # 联机房间
    ROOM = "com.demo:id/et_tryRoom"
    # 游戏ID
    GID = "com.demo:id/gidEt"
    # 用户信息
    USER = "com.demo:id/username"
    # steam参数
    STEAM = "com.demo:id/et_steam"
    # FPS选择
    FPS_SELECTOR = "com.demo:id/spinner_fps"
    # 30fps
    FPS_30 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]"
    # 60fps
    FPS_60 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]"
    # 120fps
    FPS_120 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]"
    # 视频分辨率选择
    VIDEO_SELECTOR = "com.demo:id/spinner1"
    # 480 video
    VIDEO_480 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]"
    # 720 video
    VIDEO_720 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]"
    # 1080 video
    VIDEO_1080 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]"
    # 1440 video
    VIDEO_1440 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[4]"
    # 4K video
    VIDEO_4k = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[5]"
    # 全屏拉伸
    FULL_SCREEN = "com.demo:id/btn_fullMode"
    # 游戏全屏
    GAME_FULL = "com.demo:id/btn_nativeFull"
    # ipv6
    IPV6 = "com.demo:id/checkBox_ipv6"
    # 静音
    MUTE = "com.demo:id/checkBox_mute"
    # 跳过鉴权
    AUTH = "com.demo:id/checkBox_auth"
    # 灰度配置
    CONFIG = "com.demo:id/checkBox_config"
    # force h265
    FORCE_265 = "com.demo:id/h265"
    # try_264
    TRY_264 = "com.demo:id/try_h264"
    # 预加载
    PRELOAD = "com.demo:id/cb_preload"
    # 本地输入法
    NATIVE_KEY = "com.demo:id/native_key"
    # 显示desc
    DESC = "com.demo:id/cb_desc"
    # usb dr
    USB_DRIVER = "com.demo:id/cb_usb_driver"
    # debug_mode
    DEBUG_MODE = "com.demo:id/cb_db_mode"
    # 手柄
    GAME_PAD = "com.demo:id/btn_gamePad"
    # 光标
    CURSOR = "com.demo:id/btn_cursor"
    # vrf
    VFR = "com.demo:id/checkBox_vfr"
    # 系统光标
    SYSTEM_MOUSE = "com.demo:id/btn_system_mouse"
    # 回调第一键值
    CMD = "com.demo:id/checkBox_cmd"
    # DumpVideo
    DUMP_VIDEO = "com.demo:id/video_dump"
    # floatView
    FLOAT_VIEW = "com.demo:id/floatView"
    # sdk输入法
    SDK_IME = "com.demo:id/sdk_ime"
    # SDK版本-小屏端
    SDK_PHONE = "com.demo:id/sdk_phone"
    # SDK版本-大屏端
    SDK_TV = "com.demo:id/sdk_tv"
    # 设备类型-phone
    DEV_PHONE = "com.demo:id/dev_phone"
    # 设备类型-tv
    DEV_TV = "com.demo:id/dev_tv"
    # 串流协议-comm
    COMMON_C = "com.demo:id/common_c"
    # 串流协议-RTC
    WEB_RTC = "com.demo:id/webrtc"
    # 串流协议-WS
    WS = "com.demo:id/websocket"
    # 串流协议-Lite
    RTC_LITE = "com.demo:id/rtc_lite"
    # 串流协议-默认
    DEFAULT = "com.demo:id/default_protocol"
    # 横竖屏-默认
    DEFAULT_ORI = "com.demo:id/default_ori"
    # 横竖屏-竖屏
    PORTRAIT = "com.demo:id/portrait"
    # 横竖屏-横屏
    LANDSCAPE = "com.demo:id/landscape"
    # 业务类型-斗鱼
    DOUYU = "com.demo:id/bus_douyu"
    # 业务类型-咪咕
    MI_GU = "com.demo:id/bus_migu"
    # 游戏类型-PC游戏
    PC_TYPE = "com.demo:id/pc_type"
    # 游戏类型-手游
    MOBILE_TYPE = "com.demo:id/mobile_type"
    # FEC
    FLEX_FEC = "com.demo:id/flexfec"
    # RTC加密
    ENCRYPTION = "com.demo:id/encryption"
    # RTC日志
    RTC_LOG = "com.demo:id/rtc_log"
    # EGL渲染
    RENDER_TYPE = "com.demo:id/renderType"
    # 禁止切屏
    CUT_SCREEN = "com.demo:id/btn_cutScreen"
    # 协助
    ASSIST = "com.demo:id/btn_assist"
    # 对战
    AGAINST = "com.demo:id/btn_against"
    # 观看
    WATCH = "com.demo:id/btn_watch"
    # 加入游戏模式-无
    JOIN_NONE = "com.demo:id/none"
    # 加入的游戏模式-切屏
    RB_CUT = "com.demo:id/rb_cut"
    # 加入的游戏模式-协助
    RB_ASSIST = "com.demo:id/rb_assist"
    # 加入的游戏模式-对战
    RB_AGAINST = "com.demo:id/rb_against"
    # 加入的游戏模式-观看
    RB_WATCH = "com.demo:id/rb_watch"
    # 加入的游戏模式-会议
    RB_MEETING = "com.demo:id/rb_meeting"
    # 登录
    LOGIN = "com.demo:id/textView"
    # 扫一扫
    SCAN_CODE = "com.demo:id/scan_code"
    # 测速
    ESTIMATE = "com.demo:id/estimate"
    # 主界面布局-滑动使用
    LAYOUT_MAIN = "com.demo:id/fl_main_layout"


class GameInfo(object):
    """游戏中调试界面"""

    # 启动失败
    RUN_FAIL = "com.demo:id/message2"
    # 启动失败-知道了按钮
    FAIL_BUTTON = "com.demo:id/button1"
    # 调试
    DEBUG = "com.demo:id/settingBtn"
    # 恢复串流
    Recovery = "com.demo:id/gameRecover"
    # 显示光标
    Cursor = "com.demo:id/btn_cursor"
    # 编码切换
    DECODE = "com.demo:id/btn_decode"
    # FPS下拉
    FPS_SELECT = "com.demo:id/spinner_fps_test"
    # 30 fps
    FPS_30 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]"
    # 60 fps
    FPS_60 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]"
    # 120 fps
    FPS_120 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]"
    # 分辨率选择
    VIDEO_SELECT = "com.demo:id/spinner_resolution_test"
    # 480
    VIDEO_480 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]"
    # 720
    VIDEO_720 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]"
    # 1080
    VIDEO_1080 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]"
    # 1440
    VIDEO_1440 = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[4]"
    # 4k
    VIDEO_4K = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[5]"
    # 右上角串流信息
    STREAM_INFO = "com.demo:id/streamInfoText"
    # 左侧信息
    LEFT_INFO = "com.demo:id/params"
    # help
    HELP = "com.demo:id/gameHelp"
    # 码率选择 高
    HIGH = "com.demo:id/high"
    # 码率选择 极高
    UNTRAL_HIGH = "com.demo:id/untralHigh"
    # 回到游戏
    BACKGAME = "com.demo:id/button2"
    # 调试窗口第二选项面板滑动
    ScrollView = "android.widget.ScrollView"
    # 调试窗口面板滑动
    SETTING_SROLL = "com.demo:id/settingPanel_sroll"
