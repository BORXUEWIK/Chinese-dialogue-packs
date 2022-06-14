init -990 python:
    store.mas_submod_utils.Submod(
        author="BORXUEWIK",#作者
        name="中文话题整合包",#mod的名字
        description="Monika对于有关中文内容的话题",#mod的简介,在"设置>子模组"就能看到了.
        version="1.0.0"
        settings_pane="cdp_settings"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="中文话题整合包",
            user_name="BORXUEWIK",
            repository_name="Chinese-dialogue-packs",
            update_dir="",
            attachment_id=None
        )
        
init 8 python:
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

init 8 python:
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
