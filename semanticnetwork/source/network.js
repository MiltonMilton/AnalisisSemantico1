var color = 'gray';
var len = undefined;
var container = document.getElementById('network');

var options = {
    nodes: {
        shape: 'dot',
        size: 30,
        font: {
            size: 12,
            color: '#ffffff'
        },
        borderWidth: 1
    },
    edges: {
        width: 2,
        font: {
            strokeWidth: 0
        }
    }
};

//options = {nodes:{font:{strokeWidth:0}}, edges:{font:{strokeWidth:0}}};

network = new vis.Network(container, getData(), options);

axios.post('localhost:8000/analizar/', {
    "documentos": [
        {
        	"claves":["leather","area"],
            "buscador": "Intelligo",
            "urls": [
                {
                    "url": "https://patents.google.com/patent/WO2011085935/en"
                }
            ]
        }
    ]} 
    )
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  }); 


function getData() {
    return {
        "status": "ok",
        "nodes": [
            {
                "group": 0,
                "id": 1,
                "label": "TOPIC: - tariff"
            },
            {
                "group": 0,
                "id": 2,
                "label": "duty"
            },
            {
                "group": 0,
                "id": 3,
                "label": "tariff"
            },
            {
                "group": 1,
                "id": 4,
                "label": "TOPIC: - steel"
            },
            {
                "group": 1,
                "id": 5,
                "label": "steel"
            },
            {
                "group": 1,
                "id": 6,
                "label": "nerve"
            },
            {
                "group": 1,
                "id": 7,
                "label": "brand"
            },
            {
                "group": 1,
                "id": 8,
                "label": "blade"
            },
            {
                "group": 1,
                "id": 9,
                "label": "sword"
            },
            {
                "group": 2,
                "id": 10,
                "label": "TOPIC: - canada"
            },
            {
                "group": 2,
                "id": 11,
                "label": "Canada"
            },
            {
                "group": 3,
                "id": 12,
                "label": "TOPIC: - business"
            },
            {
                "group": 3,
                "id": 13,
                "label": "patronage"
            },
            {
                "group": 3,
                "id": 14,
                "label": "commercial_enterprise"
            },
            {
                "group": 3,
                "id": 15,
                "label": "business_sector"
            },
            {
                "group": 3,
                "id": 16,
                "label": "business"
            },
            {
                "group": 3,
                "id": 17,
                "label": "line_of_work"
            },
            {
                "group": 3,
                "id": 18,
                "label": "business_enterprise"
            },
            {
                "group": 3,
                "id": 19,
                "label": "clientele"
            },
            {
                "group": 3,
                "id": 20,
                "label": "job"
            },
            {
                "group": 3,
                "id": 21,
                "label": "business_concern"
            },
            {
                "group": 3,
                "id": 22,
                "label": "business_organization"
            },
            {
                "group": 3,
                "id": 23,
                "label": "stage_business"
            },
            {
                "group": 3,
                "id": 24,
                "label": "business_organisation"
            },
            {
                "group": 3,
                "id": 25,
                "label": "occupation"
            },
            {
                "group": 3,
                "id": 26,
                "label": "byplay"
            },
            {
                "group": 3,
                "id": 27,
                "label": "line"
            },
            {
                "group": 3,
                "id": 28,
                "label": "concern"
            },
            {
                "group": 4,
                "id": 29,
                "label": "TOPIC: - bbc"
            },
            {
                "group": 5,
                "id": 30,
                "label": "TOPIC: - news"
            },
            {
                "group": 5,
                "id": 31,
                "label": "news_program"
            },
            {
                "group": 5,
                "id": 32,
                "label": "news_show"
            },
            {
                "group": 5,
                "id": 33,
                "label": "word"
            },
            {
                "group": 5,
                "id": 34,
                "label": "intelligence"
            },
            {
                "group": 5,
                "id": 35,
                "label": "tidings"
            },
            {
                "group": 5,
                "id": 36,
                "label": "newsworthiness"
            },
            {
                "group": 5,
                "id": 37,
                "label": "news"
            },
            {
                "group": 6,
                "id": 38,
                "label": "TOPIC: - say"
            },
            {
                "group": 6,
                "id": 39,
                "label": "enunciate"
            },
            {
                "group": 6,
                "id": 40,
                "label": "sound_out"
            },
            {
                "group": 6,
                "id": 41,
                "label": "read"
            },
            {
                "group": 6,
                "id": 42,
                "label": "pronounce"
            },
            {
                "group": 6,
                "id": 43,
                "label": "state"
            },
            {
                "group": 6,
                "id": 44,
                "label": "articulate"
            },
            {
                "group": 6,
                "id": 45,
                "label": "order"
            },
            {
                "group": 6,
                "id": 46,
                "label": "say"
            },
            {
                "group": 6,
                "id": 47,
                "label": "suppose"
            },
            {
                "group": 6,
                "id": 48,
                "label": "enjoin"
            },
            {
                "group": 6,
                "id": 49,
                "label": "aver"
            },
            {
                "group": 6,
                "id": 50,
                "label": "allege"
            },
            {
                "group": 6,
                "id": 51,
                "label": "tell"
            },
            {
                "group": 6,
                "id": 52,
                "label": "enounce"
            },
            {
                "group": 7,
                "id": 53,
                "label": "TOPIC: - trade"
            },
            {
                "group": 7,
                "id": 54,
                "label": "patronage"
            },
            {
                "group": 7,
                "id": 55,
                "label": "sell"
            },
            {
                "group": 7,
                "id": 56,
                "label": "barter"
            },
            {
                "group": 7,
                "id": 57,
                "label": "deal"
            },
            {
                "group": 7,
                "id": 58,
                "label": "trade"
            },
            {
                "group": 7,
                "id": 59,
                "label": "switch"
            },
            {
                "group": 7,
                "id": 60,
                "label": "craft"
            },
            {
                "group": 7,
                "id": 61,
                "label": "swap"
            },
            {
                "group": 7,
                "id": 62,
                "label": "business_deal"
            },
            {
                "group": 7,
                "id": 63,
                "label": "trade_in"
            },
            {
                "group": 7,
                "id": 64,
                "label": "swop"
            },
            {
                "group": 7,
                "id": 65,
                "label": "trade_wind"
            },
            {
                "group": 7,
                "id": 66,
                "label": "merchandise"
            },
            {
                "group": 8,
                "id": 67,
                "label": "TOPIC: - share"
            },
            {
                "group": 8,
                "id": 68,
                "label": "parcel"
            },
            {
                "group": 8,
                "id": 69,
                "label": "divvy_up"
            },
            {
                "group": 8,
                "id": 70,
                "label": "partake_in"
            },
            {
                "group": 8,
                "id": 71,
                "label": "portion_out"
            },
            {
                "group": 8,
                "id": 72,
                "label": "share"
            },
            {
                "group": 8,
                "id": 73,
                "label": "ploughshare"
            },
            {
                "group": 8,
                "id": 74,
                "label": "deal"
            },
            {
                "group": 8,
                "id": 75,
                "label": "portion"
            },
            {
                "group": 8,
                "id": 76,
                "label": "part"
            },
            {
                "group": 8,
                "id": 77,
                "label": "plowshare"
            },
            {
                "group": 8,
                "id": 78,
                "label": "partake"
            },
            {
                "group": 8,
                "id": 79,
                "label": "contribution"
            },
            {
                "group": 8,
                "id": 80,
                "label": "percentage"
            },
            {
                "group": 8,
                "id": 81,
                "label": "apportion"
            },
            {
                "group": 9,
                "id": 82,
                "label": "TOPIC: - world"
            },
            {
                "group": 9,
                "id": 83,
                "label": "planetary"
            },
            {
                "group": 9,
                "id": 84,
                "label": "domain"
            },
            {
                "group": 9,
                "id": 85,
                "label": "worldly_concern"
            },
            {
                "group": 9,
                "id": 86,
                "label": "globe"
            },
            {
                "group": 9,
                "id": 87,
                "label": "creation"
            },
            {
                "group": 9,
                "id": 88,
                "label": "humans"
            },
            {
                "group": 9,
                "id": 89,
                "label": "global"
            },
            {
                "group": 9,
                "id": 90,
                "label": "world-wide"
            },
            {
                "group": 9,
                "id": 91,
                "label": "existence"
            },
            {
                "group": 9,
                "id": 92,
                "label": "earth"
            },
            {
                "group": 9,
                "id": 93,
                "label": "populace"
            },
            {
                "group": 9,
                "id": 94,
                "label": "reality"
            },
            {
                "group": 9,
                "id": 95,
                "label": "public"
            },
            {
                "group": 9,
                "id": 96,
                "label": "humankind"
            },
            {
                "group": 9,
                "id": 97,
                "label": "humanity"
            },
            {
                "group": 9,
                "id": 98,
                "label": "worldwide"
            },
            {
                "group": 9,
                "id": 99,
                "label": "earthly_concern"
            },
            {
                "group": 9,
                "id": 100,
                "label": "macrocosm"
            },
            {
                "group": 9,
                "id": 101,
                "label": "mankind"
            },
            {
                "group": 9,
                "id": 102,
                "label": "human_beings"
            },
            {
                "group": 9,
                "id": 103,
                "label": "world"
            },
            {
                "group": 9,
                "id": 104,
                "label": "man"
            },
            {
                "group": 9,
                "id": 105,
                "label": "universe"
            },
            {
                "group": 9,
                "id": 106,
                "label": "human_race"
            },
            {
                "group": 9,
                "id": 107,
                "label": "Earth"
            },
            {
                "group": 9,
                "id": 108,
                "label": "cosmos"
            },
            {
                "group": 10,
                "id": 109,
                "label": "TOPIC: - device"
            },
            {
                "group": 10,
                "id": 110,
                "label": "device"
            },
            {
                "group": 10,
                "id": 111,
                "label": "twist"
            },
            {
                "group": 10,
                "id": 112,
                "label": "gimmick"
            },
            {
                "group": 11,
                "id": 113,
                "label": "TOPIC: - automation"
            },
            {
                "group": 11,
                "id": 114,
                "label": "mechanization"
            },
            {
                "group": 11,
                "id": 115,
                "label": "mechanisation"
            },
            {
                "group": 11,
                "id": 116,
                "label": "automation"
            },
            {
                "group": 12,
                "id": 117,
                "label": "TOPIC: - datum"
            },
            {
                "group": 12,
                "id": 118,
                "label": "data_point"
            },
            {
                "group": 12,
                "id": 119,
                "label": "datum"
            },
            {
                "group": 13,
                "id": 120,
                "label": "TOPIC: - system"
            },
            {
                "group": 13,
                "id": 121,
                "label": "organisation"
            },
            {
                "group": 13,
                "id": 122,
                "label": "system"
            },
            {
                "group": 13,
                "id": 123,
                "label": "arrangement"
            },
            {
                "group": 13,
                "id": 124,
                "label": "organization"
            },
            {
                "group": 13,
                "id": 125,
                "label": "scheme"
            },
            {
                "group": 13,
                "id": 126,
                "label": "system_of_rules"
            },
            {
                "group": 14,
                "id": 127,
                "label": "TOPIC: - property"
            },
            {
                "group": 14,
                "id": 128,
                "label": "attribute"
            },
            {
                "group": 14,
                "id": 129,
                "label": "prop"
            },
            {
                "group": 14,
                "id": 130,
                "label": "place"
            },
            {
                "group": 14,
                "id": 131,
                "label": "holding"
            },
            {
                "group": 14,
                "id": 132,
                "label": "belongings"
            },
            {
                "group": 14,
                "id": 133,
                "label": "property"
            },
            {
                "group": 14,
                "id": 134,
                "label": "dimension"
            },
            {
                "group": 15,
                "id": 135,
                "label": "TOPIC: - specific"
            },
            {
                "group": 15,
                "id": 136,
                "label": "specific"
            },
            {
                "group": 15,
                "id": 137,
                "label": "particular"
            },
            {
                "group": 16,
                "id": 138,
                "label": "TOPIC: - controller"
            },
            {
                "group": 16,
                "id": 139,
                "label": "control"
            },
            {
                "group": 16,
                "id": 140,
                "label": "accountant"
            },
            {
                "group": 16,
                "id": 141,
                "label": "restrainer"
            },
            {
                "group": 16,
                "id": 142,
                "label": "comptroller"
            },
            {
                "group": 16,
                "id": 143,
                "label": "controller"
            },
            {
                "group": 17,
                "id": 144,
                "label": "TOPIC: - method"
            },
            {
                "group": 17,
                "id": 145,
                "label": "method_acting"
            },
            {
                "group": 17,
                "id": 146,
                "label": "method"
            },
            {
                "group": 18,
                "id": 147,
                "label": "TOPIC: - programmable"
            },
            {
                "group": 19,
                "id": 148,
                "label": "TOPIC: - server"
            },
            {
                "group": 19,
                "id": 149,
                "label": "waiter"
            },
            {
                "group": 19,
                "id": 150,
                "label": "host"
            },
            {
                "group": 19,
                "id": 151,
                "label": "server"
            }
        ],
        "edges": [
            {
                "to": 1,
                "from": 2
            },
            {
                "to": 1,
                "from": 3
            },
            {
                "to": 4,
                "from": 5
            },
            {
                "to": 4,
                "from": 6
            },
            {
                "to": 4,
                "from": 7
            },
            {
                "to": 4,
                "from": 8
            },
            {
                "to": 4,
                "from": 9
            },
            {
                "to": 10,
                "from": 11
            },
            {
                "to": 12,
                "from": 13
            },
            {
                "to": 12,
                "from": 14
            },
            {
                "to": 12,
                "from": 15
            },
            {
                "to": 12,
                "from": 16
            },
            {
                "to": 12,
                "from": 17
            },
            {
                "to": 12,
                "from": 18
            },
            {
                "to": 12,
                "from": 19
            },
            {
                "to": 12,
                "from": 20
            },
            {
                "to": 12,
                "from": 21
            },
            {
                "to": 12,
                "from": 22
            },
            {
                "to": 12,
                "from": 23
            },
            {
                "to": 12,
                "from": 24
            },
            {
                "to": 12,
                "from": 25
            },
            {
                "to": 12,
                "from": 26
            },
            {
                "to": 12,
                "from": 27
            },
            {
                "to": 12,
                "from": 28
            },
            {
                "to": 30,
                "from": 31
            },
            {
                "to": 30,
                "from": 32
            },
            {
                "to": 30,
                "from": 33
            },
            {
                "to": 30,
                "from": 34
            },
            {
                "to": 30,
                "from": 35
            },
            {
                "to": 30,
                "from": 36
            },
            {
                "to": 30,
                "from": 37
            },
            {
                "to": 38,
                "from": 39
            },
            {
                "to": 38,
                "from": 40
            },
            {
                "to": 38,
                "from": 41
            },
            {
                "to": 38,
                "from": 42
            },
            {
                "to": 38,
                "from": 43
            },
            {
                "to": 38,
                "from": 44
            },
            {
                "to": 38,
                "from": 45
            },
            {
                "to": 38,
                "from": 46
            },
            {
                "to": 38,
                "from": 47
            },
            {
                "to": 38,
                "from": 48
            },
            {
                "to": 38,
                "from": 49
            },
            {
                "to": 38,
                "from": 50
            },
            {
                "to": 38,
                "from": 51
            },
            {
                "to": 38,
                "from": 52
            },
            {
                "to": 53,
                "from": 54
            },
            {
                "to": 53,
                "from": 55
            },
            {
                "to": 53,
                "from": 56
            },
            {
                "to": 53,
                "from": 57
            },
            {
                "to": 53,
                "from": 58
            },
            {
                "to": 53,
                "from": 59
            },
            {
                "to": 53,
                "from": 60
            },
            {
                "to": 53,
                "from": 61
            },
            {
                "to": 53,
                "from": 62
            },
            {
                "to": 53,
                "from": 63
            },
            {
                "to": 53,
                "from": 64
            },
            {
                "to": 53,
                "from": 65
            },
            {
                "to": 53,
                "from": 66
            },
            {
                "to": 67,
                "from": 68
            },
            {
                "to": 67,
                "from": 69
            },
            {
                "to": 67,
                "from": 70
            },
            {
                "to": 67,
                "from": 71
            },
            {
                "to": 67,
                "from": 72
            },
            {
                "to": 67,
                "from": 73
            },
            {
                "to": 67,
                "from": 74
            },
            {
                "to": 67,
                "from": 75
            },
            {
                "to": 67,
                "from": 76
            },
            {
                "to": 67,
                "from": 77
            },
            {
                "to": 67,
                "from": 78
            },
            {
                "to": 67,
                "from": 79
            },
            {
                "to": 67,
                "from": 80
            },
            {
                "to": 67,
                "from": 81
            },
            {
                "to": 82,
                "from": 83
            },
            {
                "to": 82,
                "from": 84
            },
            {
                "to": 82,
                "from": 85
            },
            {
                "to": 82,
                "from": 86
            },
            {
                "to": 82,
                "from": 87
            },
            {
                "to": 82,
                "from": 88
            },
            {
                "to": 82,
                "from": 89
            },
            {
                "to": 82,
                "from": 90
            },
            {
                "to": 82,
                "from": 91
            },
            {
                "to": 82,
                "from": 92
            },
            {
                "to": 82,
                "from": 93
            },
            {
                "to": 82,
                "from": 94
            },
            {
                "to": 82,
                "from": 95
            },
            {
                "to": 82,
                "from": 96
            },
            {
                "to": 82,
                "from": 97
            },
            {
                "to": 82,
                "from": 98
            },
            {
                "to": 82,
                "from": 99
            },
            {
                "to": 82,
                "from": 100
            },
            {
                "to": 82,
                "from": 101
            },
            {
                "to": 82,
                "from": 102
            },
            {
                "to": 82,
                "from": 103
            },
            {
                "to": 82,
                "from": 104
            },
            {
                "to": 82,
                "from": 105
            },
            {
                "to": 82,
                "from": 106
            },
            {
                "to": 82,
                "from": 107
            },
            {
                "to": 82,
                "from": 108
            },
            {
                "to": 109,
                "from": 110
            },
            {
                "to": 109,
                "from": 111
            },
            {
                "to": 109,
                "from": 112
            },
            {
                "to": 113,
                "from": 114
            },
            {
                "to": 113,
                "from": 115
            },
            {
                "to": 113,
                "from": 116
            },
            {
                "to": 117,
                "from": 118
            },
            {
                "to": 117,
                "from": 119
            },
            {
                "to": 120,
                "from": 121
            },
            {
                "to": 120,
                "from": 122
            },
            {
                "to": 120,
                "from": 123
            },
            {
                "to": 120,
                "from": 124
            },
            {
                "to": 120,
                "from": 125
            },
            {
                "to": 120,
                "from": 126
            },
            {
                "to": 127,
                "from": 128
            },
            {
                "to": 127,
                "from": 129
            },
            {
                "to": 127,
                "from": 130
            },
            {
                "to": 127,
                "from": 131
            },
            {
                "to": 127,
                "from": 132
            },
            {
                "to": 127,
                "from": 133
            },
            {
                "to": 127,
                "from": 134
            },
            {
                "to": 135,
                "from": 136
            },
            {
                "to": 135,
                "from": 137
            },
            {
                "to": 138,
                "from": 139
            },
            {
                "to": 138,
                "from": 140
            },
            {
                "to": 138,
                "from": 141
            },
            {
                "to": 138,
                "from": 142
            },
            {
                "to": 138,
                "from": 143
            },
            {
                "to": 144,
                "from": 145
            },
            {
                "to": 144,
                "from": 146
            },
            {
                "to": 148,
                "from": 149
            },
            {
                "to": 148,
                "from": 150
            },
            {
                "to": 148,
                "from": 151
            }
        ]
    }
}