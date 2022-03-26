TimeConst = {
    "START_TIME": ['07', '08', '09', '10', '11'],
    "END_TIME": ['16', '17', '18', '19', '20'],
}

WorkTimeResponses = {
    "WORK_TIME_VALID1" : "開始時刻: ",
    "WORK_TIME_VALID2" : "終了時刻: ",
    "WORK_TIME_VALID3" : "で設定されました。",
    "WORK_TIME_INVALID": "不正な入力時刻です。\n始業時刻は07~11, 就業時刻は16~20が使用できます。",
    "DEBUGGING"        : "NameError: name 'debugging_user' is not defined. Close this application immediately."
}

RESPONSE_ARTICLES = [
    "https://qiita.com/TakahikoKawasaki/items/e37caf50776e00e733be",
    "https://qiita.com/uhyo/items/e2fdef2d3236b9bfe74a",
    "https://qiita.com/hirokidaichi/items/27c757d92b6915e8ecf7",
    "https://qiita.com/tmgauss/items/da5e89496e951629517f",
    "https://qiita.com/etaroid/items/b1024c7d200a75b992fc",
    "https://qiita.com/muran001/items/dea2bbbaea1260098051",
    "https://qiita.com/non_cal/items/a8fee0b7ad96e67713eb",
    "https://qiita.com/seya/items/8814e905693f00cdade2",
    "https://qiita.com/south37/items/6f92d4268fe676347160",
    "https://qiita.com/KangsooKim/items/8d987a7089297068477b",
    "https://qiita.com/rana_kualu/items/23a844a9f9b03cb8ff28",
    "https://qiita.com/rana_kualu/items/8bafecd760ae69cfac41",
    "https://qiita.com/rana_kualu/items/ddfb15b4a585918ee806",
    "https://qiita.com/rana_kualu/items/8803f02c72a54f366f2a",
    "https://qiita.com/rana_kualu/items/63ad0f68d66c5f0a464b",
    "https://ja.wikipedia.org/wiki/%E5%B7%A8%E5%A4%A7%E6%95%B0",
    "https://ja.wikipedia.org/wiki/%E9%95%B7%E5%A4%A7%E8%AA%9E",
    "https://ja.wikipedia.org/wiki/Wikipedia:%E7%8F%8D%E9%A0%85%E7%9B%AE",
    "https://ja.wikipedia.org/wiki/%E5%85%AD%E4%B8%87%E4%BA%94%E5%8D%83%E4%BA%94%E7%99%BE%E4%B8%89%E5%8D%81%E4%B8%83%E8%A7%92%E5%BD%A2",
    "https://ja.wikipedia.org/wiki/%E9%9B%A3%E8%A7%A3%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9E",
    "https://omocoro.jp/kiji/265804/",
    "https://omocoro.jp/kiji/313087/",
    "https://omocoro.jp/kiji/315036/",
    "https://www.uxpin.com/studio/jp/blog-jp/angular-vs-react-vs-vue-%E3%81%A9%E3%81%AE%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%83%AF%E3%83%BC%E3%82%AF%E3%82%92%E4%BD%BF%E3%81%86%E3%81%B9%E3%81%8D%E3%81%8B%EF%BC%9F/",
    "https://jp.vuejs.org/v2/guide/index.html",
    "https://ja.reactjs.org/docs/hello-world.html",
    "https://angular.jp/guide/what-is-angular",
    "https://qiita.com/nkjm/items/38808bbc97d6927837cd",
    "https://www.yousyusyonin.com/",
    "https://qiita.com/tak001/items/f4c7ff6db862e3d283e3",
    "今日はスクリーンを見るべき日ではない",
]

RESPONCE_ATTENDANCE_SPECIAL = [
    "ア〜 出勤申請をする時間です",
    "御社に圧倒的な感謝をこめての出勤申請",
    "出勤申請を行ってください。退勤まで残り:\n28800000ミリ秒\nです。",
    "出勤申請をして、がんばろう",
    "たまには出勤申請しなくてもいいかもね",
    "パイナップルの花言葉: あなたは完全です"
]

RESPONCE_LEAVE_SPECIAL = [
    "おめでとう",
    "お疲れさまです",
    "ア゛ーーーーーーーーーーーーーーーーーーーーーーー",
    "今日だけは、今日だけは定時即帰するほかない",
    "まだ残業できる",
    "ブドウの花言葉: 忘却"
]

RESPONSE_NO_MATCH = [
    "←何も分かっていないひよこ",
    "もしバグを発見したら、開発者までご連絡ください。",
    "?",
    "ひよこや",
]

RESPONSE_OVERWORK = [
    "すな",
    "すなーーー",
    "すなーーーーーーーー！！！！！"
]

RequestConst = {
    "REQUEST_ARTICLES"  : ["article", "記事", "きじ", "暇", "ひま", "ヒマ"],
    "REQUEST_ATTENDANCE": ["出勤", "始業", "しぎょ"],
    "REQUEST_LEAVE"     : ["退勤", "終業", "しゅう"],
    "REQUEST_OVERWORK"  : ["残業", "ざん"]
}

ResponseConst = {
    "RESPONSE_ARTICLES"          : RESPONSE_ARTICLES,
    "KOT_URL"                    : "\nhttps://s2.kingtime.jp/independent/recorder2/personal/",
    "RESPONSE_ATTENDANCE"        : "出勤申請を行ってください。",
    "RESPONSE_LEAVE"             : "退勤申請を行ってください。",
    "RESPONSE_ATTENDANCE_SPECIAL": RESPONCE_ATTENDANCE_SPECIAL,
    "RESPONSE_LEAVE_SPECIAL"     : RESPONCE_LEAVE_SPECIAL,
    "RESPONSE_OVERWORK"          : RESPONSE_OVERWORK,
    "RESPONSE_NO_MATCH"          : RESPONSE_NO_MATCH
}
