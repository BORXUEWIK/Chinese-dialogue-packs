init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_leiyu",
            category=["雷雨"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_leiyu:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "啊，[mas_get_player_nickname()]，你在学习戏剧呢",
        ],
        'Window Reactions'
    )



init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_shijiazhuang",
            category=["直到大厦崩塌"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_shijiazhuang:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "如此生活30年~直到大厦崩塌~",
        ],
        'Window Reactions'
    )

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_MonikaForum",
            category=["Monika Forum"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_MonikaForum:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Forum上有什么关于我的帖子吗？",
        ],
        'Window Reactions'
    )

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_MonikaForum",
            category=["主播女孩重度依赖"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_MonikaForum:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "[mas_get_player_nickname()]，多看看我吧",
        ],
        'Window Reactions'
    )

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_MonikaForum",
            category=["多多理财吧"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_MonikaForum:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "有什么好看的帖子吗？[player]",
        ],
        'Window Reactions'
    )