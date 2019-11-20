from flask import Flask,request,render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/movies")
def movies():
    dict = {
    "count": 20,
    "start": 0,
    "total": 29,
    "subjects": [
        {
            "rating": {
                "max": 10,
                "average": 8.9,
                "stars": "45",
                "min": 0
            },
            "genres": [
                "\u52a8\u4f5c",
                "\u79d1\u5e7b",
                "\u5192\u9669"
            ],
            "title": "\u5934\u53f7\u73a9\u5bb6",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1328390\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1464678182.3.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1464678182.3.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1464678182.3.webp"
                    },
                    "name": "\u6cf0\u4f0a\u00b7\u8c22\u91cc\u4e39",
                    "id": "1328390"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1327806\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p8u95Rxw3ebIcel_avatar_uploaded1365073023.28.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p8u95Rxw3ebIcel_avatar_uploaded1365073023.28.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p8u95Rxw3ebIcel_avatar_uploaded1365073023.28.webp"
                    },
                    "name": " \u5965\u5229\u7ef4\u4e9a\u00b7\u5e93\u514b",
                    "id": "1327806"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1000248\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p5681.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p5681.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p5681.webp"
                    },
                    "name": "\u672c\u00b7\u95e8\u5fb7\u5c14\u68ee",
                    "id": "1000248"
                }
            ],
            "collect_count": 338142,
            "original_title": "Ready Player One",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1054440\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p34602.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p34602.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p34602.webp"
                    },
                    "name": "\u53f2\u8482\u6587\u00b7\u65af\u76ae\u5c14\u4f2f\u683c",
                    "id": "1054440"
                }
            ],
            "year": "2018",
            "images": {
                "small": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2516578307.webp",
                "large": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2516578307.webp",
                "medium": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2516578307.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/4920389\/",
            "id": "4920389"
        },
        {
            "rating": {
                "max": 10,
                "average": 8.1,
                "stars": "40",
                "min": 0
            },
            "genres": [
                "\u5267\u60c5",
                "\u559c\u5267"
            ],
            "title": "\u8d77\u8dd1\u7ebf",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1108861\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p48861.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p48861.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p48861.webp"
                    },
                    "name": "\u4f0a\u5c14\u51e1\u00b7\u53ef\u6c57",
                    "id": "1108861"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1263714\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1477506649.77.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1477506649.77.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1477506649.77.webp"
                    },
                    "name": "\u8428\u5df4\u00b7\u5361\u739b\u5c14",
                    "id": "1263714"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1049993\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1521775712.45.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1521775712.45.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1521775712.45.webp"
                    },
                    "name": "\u5185\u54c8\u00b7\u8fea\u80e1\u76ae\u963f",
                    "id": "1049993"
                }
            ],
            "collect_count": 41377,
            "original_title": "Hindi Medium",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1383681\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1510019957.97.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1510019957.97.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1510019957.97.webp"
                    },
                    "name": "\u8428\u57fa\u7279\u00b7\u4e54\u675c\u91cc",
                    "id": "1383681"
                }
            ],
            "year": "2017",
            "images": {
                "small": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517518428.webp",
                "large": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517518428.webp",
                "medium": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517518428.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/26942631\/",
            "id": "26942631"
        },
        {
            "rating": {
                "max": 10,
                "average": 8.3,
                "stars": "45",
                "min": 0
            },
            "genres": [
                "\u5267\u60c5",
                "\u72af\u7f6a",
                "\u60ac\u7591"
            ],
            "title": "\u66b4\u88c2\u65e0\u58f0",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1316200\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1449349437.71.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1449349437.71.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1449349437.71.webp"
                    },
                    "name": "\u5b8b\u6d0b",
                    "id": "1316200"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1274290\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p27203.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p27203.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p27203.webp"
                    },
                    "name": "\u59dc\u6b66",
                    "id": "1274290"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1274820\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p6464.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p6464.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p6464.webp"
                    },
                    "name": "\u8881\u6587\u5eb7",
                    "id": "1274820"
                }
            ],
            "collect_count": 54770,
            "original_title": "\u66b4\u88c2\u65e0\u58f0",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1341214\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1513848601.01.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1513848601.01.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1513848601.01.webp"
                    },
                    "name": "\u5ffb\u94b0\u5764",
                    "id": "1341214"
                }
            ],
            "year": "2017",
            "images": {
                "small": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517333671.webp",
                "large": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517333671.webp",
                "medium": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517333671.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/26647117\/",
            "id": "26647117"
        },
        {
            "rating": {
                "max": 10,
                "average": 5.8,
                "stars": "30",
                "min": 0
            },
            "genres": [
                "\u52a8\u4f5c",
                "\u79d1\u5e7b",
                "\u5192\u9669"
            ],
            "title": "\u73af\u592a\u5e73\u6d0b\uff1a\u96f7\u9706\u518d\u8d77",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1339915\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1447164061.84.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1447164061.84.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1447164061.84.webp"
                    },
                    "name": "\u7ea6\u7ff0\u00b7\u535a\u8036\u52a0",
                    "id": "1339915"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1000188\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1418720473.76.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1418720473.76.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1418720473.76.webp"
                    },
                    "name": "\u65af\u79d1\u7279\u00b7\u4f0a\u65af\u7279\u4f0d\u5fb7",
                    "id": "1000188"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1362560\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1479205212.79.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1479205212.79.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1479205212.79.webp"
                    },
                    "name": "\u5361\u8389\u00b7\u53f2\u6d3e\u59ae",
                    "id": "1362560"
                }
            ],
            "collect_count": 85518,
            "original_title": "Pacific Rim: Uprising",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1340823\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/pqiCuEHOtvNIcel_avatar_uploaded1403339434.41.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/pqiCuEHOtvNIcel_avatar_uploaded1403339434.41.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/pqiCuEHOtvNIcel_avatar_uploaded1403339434.41.webp"
                    },
                    "name": "\u65af\u8482\u6587\u00b7S\u00b7\u8fea\u5948\u7279",
                    "id": "1340823"
                }
            ],
            "year": "2018",
            "images": {
                "small": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2512933684.webp",
                "large": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2512933684.webp",
                "medium": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2512933684.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/20435622\/",
            "id": "20435622"
        },
        {
            "rating": {
                "max": 10,
                "average": 8.5,
                "stars": "45",
                "min": 0
            },
            "genres": [
                "\u5267\u60c5",
                "\u52a8\u4f5c",
                "\u72af\u7f6a"
            ],
            "title": "\u7ea2\u6d77\u884c\u52a8",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1274761\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1489386626.47.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1489386626.47.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1489386626.47.webp"
                    },
                    "name": "\u5f20\u8bd1",
                    "id": "1274761"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1354442\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1458138265.51.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1458138265.51.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1458138265.51.webp"
                    },
                    "name": "\u9ec4\u666f\u745c",
                    "id": "1354442"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1272245\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p49399.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p49399.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p49399.webp"
                    },
                    "name": "\u6d77\u6e05",
                    "id": "1272245"
                }
            ],
            "collect_count": 363632,
            "original_title": "\u7ea2\u6d77\u884c\u52a8",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1275075\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1372934445.18.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1372934445.18.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1372934445.18.webp"
                    },
                    "name": "\u6797\u8d85\u8d24",
                    "id": "1275075"
                }
            ],
            "year": "2018",
            "images": {
                "small": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2514119443.webp",
                "large": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2514119443.webp",
                "medium": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2514119443.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/26861685\/",
            "id": "26861685"
        },
        {
            "rating": {
                "max": 10,
                "average": 4.4,
                "stars": "25",
                "min": 0
            },
            "genres": [
                "\u52a8\u753b",
                "\u5192\u9669",
                "\u5bb6\u5ead"
            ],
            "title": "\u51b0\u96ea\u5973\u738b3\uff1a\u706b\u4e0e\u51b0",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1059406\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p20303.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p20303.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p20303.webp"
                    },
                    "name": "\u8fea\u00b7\u5e03\u62c9\u96f7\u00b7\u8d1d\u514b\u5c14",
                    "id": "1059406"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1390987\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/f\/movie\/ca527386eb8c4e325611e22dfcb04cc116d6b423\/pics\/movie\/celebrity-default-small.png",
                        "large": "https://img3.doubanio.com\/f\/movie\/63acc16ca6309ef191f0378faf793d1096a3e606\/pics\/movie\/celebrity-default-large.png",
                        "medium": "https://img1.doubanio.com\/f\/movie\/8dd0c794499fe925ae2ae89ee30cd225750457b4\/pics\/movie\/celebrity-default-medium.png"
                    },
                    "name": "\u6d1b\u745e\u00b7\u52a0\u7eb3",
                    "id": "1390987"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1390988\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/f\/movie\/ca527386eb8c4e325611e22dfcb04cc116d6b423\/pics\/movie\/celebrity-default-small.png",
                        "large": "https://img3.doubanio.com\/f\/movie\/63acc16ca6309ef191f0378faf793d1096a3e606\/pics\/movie\/celebrity-default-large.png",
                        "medium": "https://img1.doubanio.com\/f\/movie\/8dd0c794499fe925ae2ae89ee30cd225750457b4\/pics\/movie\/celebrity-default-medium.png"
                    },
                    "name": "Devin Bailey Griffin",
                    "id": "1390988"
                }
            ],
            "collect_count": 622,
            "original_title": "\u0421\u043d\u0435\u0436\u043d\u0430\u044f \u043a\u043e\u0440\u043e\u043b\u0435\u0432\u0430 3: \u041e\u0433\u043e\u043d\u044c \u0438 \u043b\u0435\u0434",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1362482\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/f\/movie\/ca527386eb8c4e325611e22dfcb04cc116d6b423\/pics\/movie\/celebrity-default-small.png",
                        "large": "https://img3.doubanio.com\/f\/movie\/63acc16ca6309ef191f0378faf793d1096a3e606\/pics\/movie\/celebrity-default-large.png",
                        "medium": "https://img1.doubanio.com\/f\/movie\/8dd0c794499fe925ae2ae89ee30cd225750457b4\/pics\/movie\/celebrity-default-medium.png"
                    },
                    "name": "\u963f\u5217\u514b\u8c22\u00b7\u7279\u65af\u8482\u65af\u6797",
                    "id": "1362482"
                }
            ],
            "year": "2016",
            "images": {
                "small": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517033932.webp",
                "large": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517033932.webp",
                "medium": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517033932.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/26588783\/",
            "id": "26588783"
        },
        {
            "rating": {
                "max": 10,
                "average": 6.8,
                "stars": "35",
                "min": 0
            },
            "genres": [
                "\u52a8\u4f5c",
                "\u72af\u7f6a",
                "\u60ca\u609a"
            ],
            "title": "\u901a\u52e4\u8425\u6551",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1031220\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p44906.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p44906.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p44906.webp"
                    },
                    "name": "\u8fde\u59c6\u00b7\u5c3c\u68ee",
                    "id": "1031220"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1053584\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p11871.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p11871.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p11871.webp"
                    },
                    "name": "\u7ef4\u62c9\u00b7\u6cd5\u7c73\u52a0",
                    "id": "1053584"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1006919\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1386481612.26.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1386481612.26.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1386481612.26.webp"
                    },
                    "name": "\u5e15\u7279\u91cc\u514b\u00b7\u5a01\u5c14\u68ee",
                    "id": "1006919"
                }
            ],
            "collect_count": 19255,
            "original_title": "The Commuter",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1214705\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p20263.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p20263.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p20263.webp"
                    },
                    "name": "\u4f50\u7c73\u00b7\u5e0c\u5c14\u62c9",
                    "id": "1214705"
                }
            ],
            "year": "2018",
            "images": {
                "small": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517770792.webp",
                "large": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517770792.webp",
                "medium": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517770792.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/7056414\/",
            "id": "7056414"
        },
        {
            "rating": {
                "max": 10,
                "average": 0,
                "stars": "00",
                "min": 0
            },
            "genres": [
                "\u7eaa\u5f55\u7247"
            ],
            "title": "\u5389\u5bb3\u4e86\uff0c\u6211\u7684\u56fd",
            "casts": [],
            "collect_count": 124,
            "original_title": "\u5389\u5bb3\u4e86\uff0c\u6211\u7684\u56fd",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1322050\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p52221.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p52221.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p52221.webp"
                    },
                    "name": "\u536b\u94c1",
                    "id": "1322050"
                }
            ],
            "year": "2018",
            "images": {
                "small": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2514293556.webp",
                "large": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2514293556.webp",
                "medium": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2514293556.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/30152451\/",
            "id": "30152451"
        },
        {
            "rating": {
                "max": 10,
                "average": 4.5,
                "stars": "25",
                "min": 0
            },
            "genres": [
                "\u559c\u5267",
                "\u7231\u60c5"
            ],
            "title": "\u5947\u8469\u6735\u6735",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1313867\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1473417780.64.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1473417780.64.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1473417780.64.webp"
                    },
                    "name": "\u5f20\u82e5\u6600",
                    "id": "1313867"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1275243\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1477464497.27.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1477464497.27.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1477464497.27.webp"
                    },
                    "name": "\u9a6c\u601d\u7eaf",
                    "id": "1275243"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1324619\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1441517265.3.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1441517265.3.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1441517265.3.webp"
                    },
                    "name": "\u674e\u73b0",
                    "id": "1324619"
                }
            ],
            "collect_count": 1693,
            "original_title": "\u5947\u8469\u6735\u6735",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1320856\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1485223315.79.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1485223315.79.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1485223315.79.webp"
                    },
                    "name": "\u674e\u6b23",
                    "id": "1320856"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1327371\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1522382442.45.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1522382442.45.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1522382442.45.webp"
                    },
                    "name": "\u674e\u6d0b",
                    "id": "1327371"
                }
            ],
            "year": "2018",
            "images": {
                "small": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517679011.webp",
                "large": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517679011.webp",
                "medium": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517679011.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/26718803\/",
            "id": "26718803"
        },
        {
            "rating": {
                "max": 10,
                "average": 6.3,
                "stars": "35",
                "min": 0
            },
            "genres": [
                "\u52a8\u753b",
                "\u5192\u9669",
                "\u5bb6\u5ead"
            ],
            "title": "\u732b\u4e0e\u6843\u82b1\u6e90",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1389747\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1520590388.09.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1520590388.09.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1520590388.09.webp"
                    },
                    "name": "\u674e\u5b87\u5cf0",
                    "id": "1389747"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1379781\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1520590401.26.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1520590401.26.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1520590401.26.webp"
                    },
                    "name": "\u6768\u781a\u94ce",
                    "id": "1379781"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1038045\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p3629.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p3629.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p3629.webp"
                    },
                    "name": "\u5468\u534e\u5065",
                    "id": "1038045"
                }
            ],
            "collect_count": 1017,
            "original_title": "\u732b\u4e0e\u6843\u82b1\u6e90",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1348285\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1480411564.71.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1480411564.71.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1480411564.71.webp"
                    },
                    "name": "\u738b\u5fae",
                    "id": "1348285"
                }
            ],
            "year": "2018",
            "images": {
                "small": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517516405.webp",
                "large": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517516405.webp",
                "medium": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517516405.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/27114911\/",
            "id": "27114911"
        },
        {
            "rating": {
                "max": 10,
                "average": 6.4,
                "stars": "35",
                "min": 0
            },
            "genres": [
                "\u52a8\u4f5c",
                "\u5192\u9669"
            ],
            "title": "\u53e4\u5893\u4e3d\u5f71\uff1a\u6e90\u8d77\u4e4b\u6218",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1233154\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1427204716.36.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1427204716.36.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1427204716.36.webp"
                    },
                    "name": "\u827e\u4e3d\u897f\u4e9a\u00b7\u7ef4\u574e\u5fb7",
                    "id": "1233154"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1027173\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p4228.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p4228.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p4228.webp"
                    },
                    "name": "\u591a\u7c73\u5c3c\u514b\u00b7\u5a01\u65af\u7279",
                    "id": "1027173"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1098551\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p50351.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p50351.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p50351.webp"
                    },
                    "name": "\u6c83\u5c14\u987f\u00b7\u6208\u91d1\u65af",
                    "id": "1098551"
                }
            ],
            "collect_count": 53870,
            "original_title": "Tomb Raider",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1051062\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1492880241.68.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1492880241.68.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1492880241.68.webp"
                    },
                    "name": "\u7f57\u963f\u5c14\u00b7\u4e4c\u7d22\u683c",
                    "id": "1051062"
                }
            ],
            "year": "2018",
            "images": {
                "small": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2512717509.webp",
                "large": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2512717509.webp",
                "medium": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2512717509.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/3445906\/",
            "id": "3445906"
        },
        {
            "rating": {
                "max": 10,
                "average": 7.2,
                "stars": "40",
                "min": 0
            },
            "genres": [
                "\u5267\u60c5",
                "\u7231\u60c5",
                "\u8fd0\u52a8"
            ],
            "title": "\u82b1\u6ed1\u5973\u738b",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1384010\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1518077039.05.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1518077039.05.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1518077039.05.webp"
                    },
                    "name": "\u963f\u683c\u62c9\u5a05\u00b7\u5854\u62c9\u7d22\u5a03",
                    "id": "1384010"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1370381\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1518077095.41.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1518077095.41.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1518077095.41.webp"
                    },
                    "name": "\u4e9a\u5386\u5c71\u5927\u00b7\u4f69\u7279\u7f57\u592b",
                    "id": "1370381"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1332438\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/pXZEBgcm0vI4cel_avatar_uploaded1375591876.94.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/pXZEBgcm0vI4cel_avatar_uploaded1375591876.94.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/pXZEBgcm0vI4cel_avatar_uploaded1375591876.94.webp"
                    },
                    "name": "\u7c73\u6d1b\u65af\u00b7\u6bd4\u67ef\u7ef4\u5947",
                    "id": "1332438"
                }
            ],
            "collect_count": 7016,
            "original_title": "\u041b\u0451\u0434",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1384009\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1518076789.91.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1518076789.91.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1518076789.91.webp"
                    },
                    "name": "\u5965\u5217\u683c\u00b7\u7279\u7f57\u8d39\u59c6",
                    "id": "1384009"
                }
            ],
            "year": "2018",
            "images": {
                "small": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517485270.webp",
                "large": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517485270.webp",
                "medium": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2517485270.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/27196380\/",
            "id": "27196380"
        },
        {
            "rating": {
                "max": 10,
                "average": 4.8,
                "stars": "25",
                "min": 0
            },
            "genres": [
                "\u5267\u60c5",
                "\u559c\u5267",
                "\u7231\u60c5"
            ],
            "title": "\u9047\u89c1\u4f60\u771f\u597d",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1332932\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/pmk5M2yEclAMcel_avatar_uploaded1376453132.87.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/pmk5M2yEclAMcel_avatar_uploaded1376453132.87.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/pmk5M2yEclAMcel_avatar_uploaded1376453132.87.webp"
                    },
                    "name": "\u767d\u5ba2",
                    "id": "1332932"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1318954\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p45514.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p45514.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p45514.webp"
                    },
                    "name": "\u84dd\u76c8\u83b9",
                    "id": "1318954"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1364842\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1481737131.45.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1481737131.45.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1481737131.45.webp"
                    },
                    "name": "\u5f20\u6d77\u5b87",
                    "id": "1364842"
                }
            ],
            "collect_count": 6265,
            "original_title": "\u9047\u89c1\u4f60\u771f\u597d",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1037747\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1423.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1423.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1423.webp"
                    },
                    "name": "\u987e\u957f\u536b",
                    "id": "1037747"
                }
            ],
            "year": "2018",
            "images": {
                "small": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2516082047.webp",
                "large": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2516082047.webp",
                "medium": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2516082047.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/26967920\/",
            "id": "26967920"
        },
        {
            "rating": {
                "max": 10,
                "average": 7.1,
                "stars": "35",
                "min": 0
            },
            "genres": [
                "\u5267\u60c5",
                "\u72af\u7f6a",
                "\u60ac\u7591"
            ],
            "title": "\u7b2c\u4e09\u5ea6\u5acc\u7591\u4eba",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1006103\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1209.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1209.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1209.webp"
                    },
                    "name": "\u798f\u5c71\u96c5\u6cbb",
                    "id": "1006103"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1165478\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1458.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1458.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1458.webp"
                    },
                    "name": "\u5f79\u6240\u5e7f\u53f8",
                    "id": "1165478"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1328056\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1475053232.53.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1475053232.53.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1475053232.53.webp"
                    },
                    "name": "\u5e7f\u6fd1\u94c3",
                    "id": "1328056"
                }
            ],
            "collect_count": 14085,
            "original_title": "\u4e09\u5ea6\u76ee\u306e\u6bba\u4eba",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1274351\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1363134033.35.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1363134033.35.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1363134033.35.webp"
                    },
                    "name": "\u662f\u679d\u88d5\u548c",
                    "id": "1274351"
                }
            ],
            "year": "2017",
            "images": {
                "small": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2516825103.webp",
                "large": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2516825103.webp",
                "medium": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2516825103.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/26952153\/",
            "id": "26952153"
        },
        {
            "rating": {
                "max": 10,
                "average": 7.5,
                "stars": "40",
                "min": 0
            },
            "genres": [
                "\u559c\u5267",
                "\u52a8\u753b",
                "\u5192\u9669"
            ],
            "title": "\u6bd4\u5f97\u5154",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1017966\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1449532609.88.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1449532609.88.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1449532609.88.webp"
                    },
                    "name": "\u8a79\u59c6\u65af\u00b7\u67ef\u767b",
                    "id": "1017966"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1313116\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1361026097.22.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1361026097.22.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1361026097.22.webp"
                    },
                    "name": "\u591a\u59c6\u7eb3\u5c14\u00b7\u683c\u91cc\u68ee",
                    "id": "1313116"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1022562\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p3186.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p3186.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p3186.webp"
                    },
                    "name": "\u841d\u4e1d\u00b7\u62dc\u6069",
                    "id": "1022562"
                }
            ],
            "collect_count": 25175,
            "original_title": "Peter Rabbit",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1274281\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p12038.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p12038.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p12038.webp"
                    },
                    "name": "\u5a01\u5c14\u00b7\u53e4\u52d2",
                    "id": "1274281"
                }
            ],
            "year": "2018",
            "images": {
                "small": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2515434674.webp",
                "large": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2515434674.webp",
                "medium": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2515434674.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/26649604\/",
            "id": "26649604"
        },
        {
            "rating": {
                "max": 10,
                "average": 7.3,
                "stars": "40",
                "min": 0
            },
            "genres": [
                "\u5267\u60c5",
                "\u7231\u60c5",
                "\u5947\u5e7b"
            ],
            "title": "\u6c34\u5f62\u7269\u8bed",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1044915\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p48056.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p48056.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p48056.webp"
                    },
                    "name": "\u838e\u8389\u00b7\u970d\u91d1\u65af",
                    "id": "1044915"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1019031\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p18795.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p18795.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p18795.webp"
                    },
                    "name": "\u9053\u683c\u00b7\u743c\u65af",
                    "id": "1019031"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1144415\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p57057.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p57057.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p57057.webp"
                    },
                    "name": "\u8fc8\u514b\u5c14\u00b7\u73ca\u519c",
                    "id": "1144415"
                }
            ],
            "collect_count": 197030,
            "original_title": "The Shape of Water",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1027182\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p4294.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p4294.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p4294.webp"
                    },
                    "name": "\u5409\u5c14\u83ab\u00b7\u5fb7\u5c14\u00b7\u6258\u7f57",
                    "id": "1027182"
                }
            ],
            "year": "2017",
            "images": {
                "small": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2515650989.webp",
                "large": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2515650989.webp",
                "medium": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2515650989.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/26752852\/",
            "id": "26752852"
        },
        {
            "rating": {
                "max": 10,
                "average": 4.8,
                "stars": "25",
                "min": 0
            },
            "genres": [
                "\u559c\u5267",
                "\u52a8\u4f5c",
                "\u60ac\u7591"
            ],
            "title": "\u6211\u8bf4\u7684\u90fd\u662f\u771f\u7684",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1274081\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p6398.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p6398.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p6398.webp"
                    },
                    "name": "\u5c0f\u6c88\u9633",
                    "id": "1274081"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1274316\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p31663.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p31663.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p31663.webp"
                    },
                    "name": "\u9648\u610f\u6db5",
                    "id": "1274316"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1314321\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p45924.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p45924.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p45924.webp"
                    },
                    "name": "\u5434\u6a3e",
                    "id": "1314321"
                }
            ],
            "collect_count": 886,
            "original_title": "\u6211\u8bf4\u7684\u90fd\u662f\u771f\u7684",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1315726\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1417885062.06.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1417885062.06.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1417885062.06.webp"
                    },
                    "name": "\u5218\u4eea\u4f1f",
                    "id": "1315726"
                }
            ],
            "year": "2018",
            "images": {
                "small": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2515774685.webp",
                "large": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2515774685.webp",
                "medium": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2515774685.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/26806316\/",
            "id": "26806316"
        },
        {
            "rating": {
                "max": 10,
                "average": 8.7,
                "stars": "45",
                "min": 0
            },
            "genres": [
                "\u5267\u60c5",
                "\u72af\u7f6a"
            ],
            "title": "\u4e09\u5757\u5e7f\u544a\u724c",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1010548\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1436865941.42.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1436865941.42.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1436865941.42.webp"
                    },
                    "name": "\u5f17\u5170\u897f\u65af\u00b7\u9ea6\u514b\u591a\u8499\u5fb7",
                    "id": "1010548"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1053560\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p501.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p501.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p501.webp"
                    },
                    "name": "\u4f0d\u8fea\u00b7\u54c8\u91cc\u68ee",
                    "id": "1053560"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1047972\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1358812490.58.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1358812490.58.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1358812490.58.webp"
                    },
                    "name": "\u5c71\u59c6\u00b7\u6d1b\u514b\u5a01\u5c14",
                    "id": "1047972"
                }
            ],
            "collect_count": 257292,
            "original_title": "Three Billboards Outside Ebbing, Missouri",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1000304\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1406649730.61.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1406649730.61.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1406649730.61.webp"
                    },
                    "name": "\u9a6c\u4e01\u00b7\u9ea6\u514b\u5510\u7eb3",
                    "id": "1000304"
                }
            ],
            "year": "2017",
            "images": {
                "small": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2510081688.webp",
                "large": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2510081688.webp",
                "medium": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2510081688.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/26611804\/",
            "id": "26611804"
        },
        {
            "rating": {
                "max": 10,
                "average": 6.6,
                "stars": "35",
                "min": 0
            },
            "genres": [
                "\u5267\u60c5"
            ],
            "title": "\u6e05\u6c34\u91cc\u7684\u5200\u5b50",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1371658\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/f\/movie\/ca527386eb8c4e325611e22dfcb04cc116d6b423\/pics\/movie\/celebrity-default-small.png",
                        "large": "https://img3.doubanio.com\/f\/movie\/63acc16ca6309ef191f0378faf793d1096a3e606\/pics\/movie\/celebrity-default-large.png",
                        "medium": "https://img1.doubanio.com\/f\/movie\/8dd0c794499fe925ae2ae89ee30cd225750457b4\/pics\/movie\/celebrity-default-medium.png"
                    },
                    "name": "\u6768\u751f\u4ed3",
                    "id": "1371658"
                }
            ],
            "collect_count": 1769,
            "original_title": "\u6e05\u6c34\u91cc\u7684\u5200\u5b50",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1371653\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1491549066.4.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1491549066.4.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1491549066.4.webp"
                    },
                    "name": "\u738b\u5b66\u535a",
                    "id": "1371653"
                }
            ],
            "year": "2016",
            "images": {
                "small": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2516999755.webp",
                "large": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2516999755.webp",
                "medium": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2516999755.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/26593732\/",
            "id": "26593732"
        },
        {
            "rating": {
                "max": 10,
                "average": 7.3,
                "stars": "40",
                "min": 0
            },
            "genres": [
                "\u5267\u60c5",
                "\u79d1\u5e7b",
                "\u60ca\u609a"
            ],
            "title": "\u6e6e\u706d",
            "casts": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1054454\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p2274.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p2274.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p2274.webp"
                    },
                    "name": "\u5a1c\u5854\u8389\u00b7\u6ce2\u7279\u66fc",
                    "id": "1054454"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1004588\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1424.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1424.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1424.webp"
                    },
                    "name": "\u8a79\u59ae\u5f17\u00b7\u6770\u68ee\u00b7\u674e",
                    "id": "1004588"
                },
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1328190\/",
                    "avatars": {
                        "small": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/pfFyUvfteUGwcel_avatar_uploaded1366276814.07.webp",
                        "large": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/pfFyUvfteUGwcel_avatar_uploaded1366276814.07.webp",
                        "medium": "https://img1.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/pfFyUvfteUGwcel_avatar_uploaded1366276814.07.webp"
                    },
                    "name": "\u5409\u5a1c\u00b7\u7f57\u5fb7\u91cc\u683c\u5179",
                    "id": "1328190"
                }
            ],
            "collect_count": 54923,
            "original_title": "Annihilation",
            "subtype": "movie",
            "directors": [
                {
                    "alt": "https:\/\/movie.douban.com\/celebrity\/1284570\/",
                    "avatars": {
                        "small": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1433647152.45.webp",
                        "large": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1433647152.45.webp",
                        "medium": "https://img3.doubanio.com\/view\/celebrity\/s_ratio_celebrity\/public\/p1433647152.45.webp"
                    },
                    "name": "\u4e9a\u5386\u514b\u65af\u00b7\u5609\u5170",
                    "id": "1284570"
                }
            ],
            "year": "2018",
            "images": {
                "small": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2516914607.webp",
                "large": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2516914607.webp",
                "medium": "https://img1.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2516914607.webp"
            },
            "alt": "https:\/\/movie.douban.com\/subject\/26384741\/",
            "id": "26384741"
        }
    ],
    "title": "\u6b63\u5728\u4e0a\u6620\u7684\u7535\u5f71-\u5317\u4eac"
}
    return json.dumps(dict)



application = app
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8008, debug=True)