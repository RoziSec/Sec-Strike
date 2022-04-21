#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : scan.py
# @Author : Norah C.IV
# @Time : 2022/4/21 10:36
# @Software: PyCharm
import nmap


class Nmap:
    def __init__(self):
        self.sim = '21,22,80,139,445,3306,3389,8080'
        self.oft = '1-2433,2492,2500,2501,2522,2525,2557,2564,2600,2601,2602,2603,2604,2605,2606,2607,2608,2627,2638,2701,2702,2710,2717,2718,2725,2766,2784,2800,2809,2811,2869,2875,2903,2909,2910,2920,2967,2968,2998,3000,3001,3003,3005,3006,3007,3011,3013,3017,3030,3031,3049,3052,3064,3071,3077,3086,3128,3130,3141,3168,3211,3221,3260,3261,3264,3268,3269,3283,3292,3296,3306,3322,3323,3324,3325,3333,3343,3346,3351,3367,3369,3370,3371,3372,3389,3390,3401,3421,3455,3456,3457,3462,3476,3493,3517,3527,3531,3551,3580,3659,3664,3689,3690,3702,3703,3737,3784,3800,3801,3809,3814,3826,3827,3828,3851,3869,3871,3878,3880,3889,3900,3905,3914,3918,3920,3945,3971,3984,3985,3986,3995,3996,3997,3998,3999,4000,4001,4002,4003,4004,4005,4006,4008,4011,4045,4080,4111,4125,4126,4129,4132,4133,4144,4224,4242,4279,4321,4333,4343,4443,4444,4445,4446,4449,4480,4500,4550,4557,4559,4567,4660,4662,4666,4672,4827,4848,4899,4900,4987,4998,5000,5001,5002,5003,5004,5009,5010,5011,5030,5050,5051,5054,5060,5061,5080,5093,5100,5101,5102,5145,5190,5191,5192,5193,5200,5221,5222,5225,5226,5232,5236,5269,5277,5280,5298,5300,5301,5302,5303,5304,5305,5308,5351,5353,5355,5357,5400,5405,5414,5428,5431,5432,5490,5500,5510,5520,5530,5540,5550,5555,5556,5560,5566,5631,5632,5633,5666,5678,5679,5680,5713,5714,5715,5716,5717,5718,5730,5800,5801,5802,5803,5859,5900,5901,5902,5903,5910,5911,5963,5977,5978,5979,5987,5988,5989,5997,5998,5999,6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6025,6050,6059,6100,6101,6103,6105,6106,6110,6111,6112,6123,6141,6142,6143,6144,6145,6146,6147,6148,6267,6346,6347,6389,6400,6401,6502,6510,6543,6544,6547,6548,6549,6558,6566,6567,6580,6588,6666,6667,6668,6669,6689,6699,6788,6789,6881,6901,6969,7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7025,7070,7100,7161,7200,7201,7273,7323,7326,7402,7443,7464,7597,7626,7627,7648,7649,7650,7651,7676,7741,7777,7778,7800,7937,7938,7999,8000,8001,8002,8007,8008,8009,8010,8021,8022,8042,8080,8081,8082,8083,8086,8087,8088,8100,8192,8193,8194,8200,8292,8300,8383,8400,8402,8443,8500,8600,8765,8800,8873,8888,8892,8899,8900,8880,8999,9000,9001,9002,9009,9010,9020,9040,9050,9080,9090,9091,9100,9101,9102,9103,9111,9152,9200,9207,9418,9500,9535,9593,9594,9595,9618,9876,9898,9900,9929,9950,9991,9992,9998,9999,10000,10001,10002,10003,10004,10005,10009,10010,10080,10082,10083,11111,11371,11720,11967,12000,12345,12346,13701,13702,13705,13706,13708,13709,13710,13711,13712,13713,13714,13715,13716,13717,13718,13720,13721,13722,13724,13782,13783,14000,15000,15126,15660,15858,16000,16001,16080,16959,16992,16993,17007,17185,17219,17300,17754,18000,18181,18182,18183,18184,18185,18187,18888,19283,19315,19541,20000,20003,20005,20031,20222,21000,21554,21800,21847,22273,22289,22305,22321,22370,25003,26000,26208,26900,27000,27001,27002,27003,27004,27005,27006,27007,27008,27009,27010,27015,27374,27444,27500,27665,27910,27960,28910,30100,31335,31337,32000,32768,32769,32770,32771,32772,32773,32774,32775,32776,32777,32778,32779,32780,32786,32787,33270,33434,33567,33568,38037,38292,38293,39213,42508,42510,43188,44334,44442,44443,45000,47557,47624,47808,49400,50000,50002,54320,54321,60008,60177,60179,61439,61440,61441,62078,65301,50070,27017,27018,2181,63957,873,5984,9300,9201,9202,11211,50030,2082,2083,3312,3311,4440,6082,6379,8089,8649,28017,1099,27137,2049,2375,50075,50060,60030,8161,61616,20880,20881,8393'
        self.all = '1-65535'

    def scan(self, port):
        nm = nmap.PortScanner()
        if port == 'sim':
            ports = self.sim
        elif port == 'oft':
            ports = self.oft
        else:
            ports = self.all
        print(ports)
