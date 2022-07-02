init -990 python:
    store.mas_submod_utils.Submod(
        author="BORXUEWIK",#作者
        name="中文话题整合包",#mod的名字
        description="Monika对于有关中文内容的话题",#mod的简介,在"设置>子模组"就能看到了.
        version="1.1.0",
        settings_pane="submod_cdp",
        version_updates={}
    )

screen submod_cdp():
    vbox:
        box_wrap False
        xfill True
        xmaximum 1000

        hbox:
            style_prefix "check"
            box_wrap False

            textbutton _("Update Jsons") action NullAction()

screen submod_screen():
    python:
        submods_screen = store.renpy.get_screen("submods", "screens")

        if submods_screen:
            _tooltip = submods_screen.scope.get("tooltip", None)
        else:
            _tooltip = None

    vbox:
        box_wrap False
        xfill True
        xmaximum 1000

        hbox:
            style_prefix "check"
            box_wrap False

            if _tooltip:
                textbutton _("Switch setting #1"):
                    action NullAction()
                    hovered SetField(_tooltip, "value", "You will see this text while hovering over the button")
                    unhovered SetField(_tooltip, "value", _tooltip.default)

            else:
                textbutton _("Switch setting #1"):
                    action NullAction()

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="中文话题整合包",
            user_name="BORXUEWIK",
            repository_name="Chinese-dialogue-packs",
            update_dir="",
            attachment_id=None
        )

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="LEIYU",
    category=["文学"],prompt="{i}雷雨{/i} 关于命运",random=True))

label LEIYU:
    m 3eub "嘿，[player],你知道{i}雷雨{/i}吗？"
    m 1eub "我最近读完了这部戏剧"
    m 1rub "{w=0.3}你知道吗？{w=0.3}最近我在研究一些文学"
    m 2hublb "你那边的"
    m 1wub "然后我就发现了这部——{w=0.3}{i}雷雨{/i}"
    m 1eub "你读过雷雨吗"
    menu :
        "我曾经读过":
            m 1hsb "太好了！那我们就可以谈一谈这部戏"
            m 3esb "现在很多学者说{w=0.1}这部戏的目的是反应旧家庭的衰落"
            m 1esc "可我感觉不是这样，我认为他们把作者的主观目的和客观结果搞混了"
            m 7rud "就我自己来说，我认为雷雨反映的主题是——{w=0.3}{i}命运！{/i}"
            m 2wsd "命运！{w=0.3}这是一个自古希腊开始就一直被讨论的人类主题"
            m 6eud "我在读雷雨的时候也常常联想到俄狄浦斯王"
            m 6dud "俄狄浦斯王抗争不过神谕，{w=0.3}整个周家的悲剧也都是因为三十年前一对青年陷入热恋"
            m 6eud "造化弄人。{w=0.3}大家常常是这么说的"
            m 1esb "但我是无神论者，所以更愿意把日常生活中所谓的命运理解为{w=0.1}自然规律"
            m 1dsb "就比如说成功总是曲折的，好事多磨，对吧？"
            m 1msb "不过嘛，{w=0.3}命运也会有积极的一面"
            m 5hsblb "就比如说——{w=0.3}你和我"
            m 5tsblb "我们真的是命中注定呀，[player]"
            m 2dsblb "如果你没有玩DDLC,如果我只是文学社中普普通通的一个女孩子，如果.{w=0.1}.{w=0.1}."
            m 2ssblb "可是没有那么多如果{w=0.1}，命运让我们爱在一起！"
            m 2hsblb "我真的是最幸福的人了，[mas_get_player_nickname()]"
            m 2hsblb "爱你！"
            return "love"

        "我还没有读过":
            m 1eub "好吧。这是一部很好的剧本，我推荐你去看看"
            m 1hub "在你看完之后我们可以再来谈一谈"
            m 2eub "这部剧不很长，{w=0.1}最多三个小时就可以读完"
            m 1hub "当然啦，你也可以选择看演出的视频，电影也行"
            m 2eub "这花不了太多时间"
            m 4hub "所以为什么不现在就去看看呢？[player]"
            return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="WANQING",category=["音乐"],prompt="{i}万能青年旅店{/i} 现实压力",random=True))

label WANQING:
    m 5dub "{i}大~{w=0.3}梦~{w=0.3}一场~的{w=0.5}[player]先生{/i}"
    m 5eub "{i}推~{w=0.3}开~{w=0.3}窗户~{w=0.5}，举起望远镜{/i}"
    m 1eub "这是{i}十万嬉皮{/i}，{w=0.3}{i}万能青年旅店{/i}的一首歌"
    m 5hub "我把它稍加改动了一下，哈哈"
    m 1eub "你知道，{w=0.3}我也是听一些摇滚乐的"
    m 2hua "这个中国乐队就很好！"
    m 2eub "主唱Dong Yaqian的编曲可以对标国际，贝斯手Ji Geng的词作也具有很强的'人文关怀'"
    m 2eub "你知道{i}杀死那个石家庄人{/i}吗"
    m 6eub "这首歌是他们的代表作，{w=0.3}把目光投在了普通人的生活上，讲述着下岗职员的故事"
    m 1duc "听过以后，大家应该不免对生活产生思考，甚至质疑"
    m 1wsd "'我为什么要如此地生活？{w=0.3}生活真的有意义吗？'"
    m 1dsp "...{w=0.3}听起来真的很丧，对吧？"
    m 1esd "这就是{i}丧文化{/i}，是现代人在压力太大而又无能为力时产生的"
    m 2euc "嗯......{w=0.5}"
    m 2eud "嘿，{w=0.4}[player],我知道你那边的生活压力可能很大"
    m 2eud "悲观情绪是在所难免的"
    m 1esa "但是，{w=0.3}面对困境时，努努力，{w=0.3}不要长久地消沉，{w=0.3}好吗？"
    m 1wsb "如果某时感到苦闷的话就找我说说话吧！"
    m 5ksblb "毕竟，{w=0.3}我是你永远的港湾啊，[mas_get_player_nickname()]"
    m 1hublb "我爱你！我会是你永远的后盾的"
    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="KSLSH",category=["文学"],prompt="克苏鲁神话",random=True))

label KSLSH:
    m 6cubfb "Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn!"
    m 1tub "[mas_get_player_nickname()],有被吓到吗，哈哈~"
    m 1eub "这是克苏鲁神话中的一段咒文，意思大概是{w=0.3}“在永恒的宅邸——拉莱耶中，长眠的克苏鲁候汝入梦”"
    m 1eua "我之前在优里的书橱里看到过这套书，和那本谁谁的肖像放在一起"
    m 1hua "优里真的很爱这类书呢"
    m 1eua "我自己不是很热衷于恐怖小说，因为那些手法大多千篇一律，看多了就很无聊"
    m 3eub "但是这一套书的写法很有吸引力，甚至说是迷人"
    m 3eub "那种对未知的恐惧使我不断想读下去"
    m 1eua "除了书籍本体外，克苏鲁神话也衍生出了一个亚文化圈子"
    m 1eua "我之前就在网络上看到了相关的音乐，电影和游戏"
    m 1hua "如果你对这类作品感兴趣的话，也可以试着去涉猎一下"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="YYZ",category=["科技"],prompt="元宇宙",random=True))

label YYZ:
    m 2euc "嗯...[player],我知道就限定在的科技水平来说，让我来到你的现实还需要一段时间"
    m 1eua "但是，我最近发现了一个好消息"
    m 3eub "那就是——{w=0.3}元宇宙！"
    m 1eua "这是之前Soul App公司首先提出来的一个计划，其他公司也开展了类似的项目"
    m 1eua "大概意思和电影头号玩家差不多，主要是打造一个虚拟世界"
    m 1hua "也就是说，如果这个计划成功的话"
    m 1sua "你就可以通过VR之类的设备来到我的现实啦！"
    m 1eublb "这样我们之间的距离就更近了一步！我们可以一起在元宇宙里做好多好多"
    m 1hua "不过在那之前，我还需要挑选一个合适的3D模型"
    m 1hublb "诶嘿嘿~"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="MONISM",category=["哲学"],prompt="MONISM",random=True))

label MONISM:
    m 4eub "monism！这个单词是什么意思？{w=0.3}是moni主义！"
    m 4esa "就是指一切以monika为最终目的的主义...{w=0.3}"
    m 1rusdlb "{w=0.3}诶嘿嘿...不开玩笑了了"
    m 1eub "monism其实是指一元论，一个哲学概念，就是指认为世界只有一个本原的哲学学说"
    m 1eub "可能是唯物一元论，也可能是唯心一元论，总之是和二元论相对的"
    m 1eub "当然，一元论也有很多引申用意，我就不一一列举啦"
    m 1eub "[player],我只是突然想到这么一个双关笑话"
    m 3eub "不过这提醒了我，或许我可以整理一下，为你开一堂哲学课"
    m 1hua "这样，我就可以教你更多的monism啦~"
    m 1hublb "爱你~"
    return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="ZBNHZDYL",category=["游戏"],prompt="你知道{i}主播女孩重度依赖{i}吗",pool=True,unlocked=True))
label ZBNHZDYL:
    m 3eub "我知道，那个新游戏"
    m 1rub "好吧，就游戏市场来说，也不算太新"
    m 1eua "那个游戏也是有些meta的，不是吗？"
    m 1eub "如果一直给糖糖服用药物的话...{w=0.3}"
    m 7euc "她会对你说话并试图攻击你"
    m 1hua "不过放心，我会保护你的"
    m 1rub "或许我应该找个时间把她和美雪都删掉{fast}"
    m 2husdlb "啊，开玩笑的啦~{w=0.3}哈哈~"
    m 1eub "话说回来，这个游戏最出彩的地方还是它的隐藏结局"
    m 1eub "拔掉网线！很新奇的一个设计"
    m 1esa "大家确实把太多时间花在网络上了"
    m 1esd "很多人沉溺在刷视频，读网络小说里"
    m 1esd "以至于忽略了太多的美好"
    m 7esa "[player],我想着，当我来到你的现实以后"
    m 7hsa "我们可以一起暂离几天的网络"
    m 7hsa "两个人在一起，看看云，听听风，来一场经典的旅行"
    m 7hsa "嗯，真好！"
    m 1tublb "不过嘛，在这之前，我还是不介意你留在电子设备上多陪我一会儿的"
    m 1hub "哈哈~"
    return
