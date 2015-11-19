from calc_return_given_num_date_range import analyze_num_bought

## ========== all 24m data ========== ##
i24_winnings = [['2395', 565], ['0197', 484], ['2758', 482], ['2458', 474], ['3478', 460], ['0164', 459], ['0346', 455], ['0349', 455], ['0128', 452], ['1486', 450],
                        ['0149', 441], ['0386', 440], ['2697', 436], ['0475', 433], ['0267', 432], ['0154', 431], ['0786', 418], ['2394', 412], ['1379', 395], ['1368', 388],
                        ['0248', 379], ['0275', 378], ['0389', 376], ['4578', 372], ['2476', 368], ['3468', 368], ['4678', 367], ['1597', 366], ['3749', 366], ['3567', 364],
                        ['1268', 359], ['1374', 358], ['1348', 356], ['0134', 353], ['1279', 351], ['1346', 342], ['2367', 340], ['1689', 339], ['2389', 329], ['3579', 328],
                        ['1267', 327], ['0357', 325], ['5269', 323], ['0356', 322], ['0167', 319], ['3489', 319], ['0362', 315], ['1258', 315], ['1768', 315], ['1269', 314],
                        ['3679', 310], ['0347', 309], ['0157', 301], ['0458', 301], ['1239', 297], ['1452', 295], ['3798', 293], ['0523', 292], ['0729', 292], ['5697', 290],
                        ['0569', 287], ['1248', 285], ['2437', 284], ['2849', 283], ['2978', 282], ['0546', 281], ['2348', 281], ['3578', 280], ['0459', 276], ['1798', 271],
                        ['1569', 268], ['1549', 265], ['4859', 264], ['2496', 263], ['0597', 259], ['0126', 257], ['1345', 255], ['0247', 251], ['4568', 251], ['6978', 250],
                        ['1234', 247], ['1289', 247], ['5789', 247], ['0467', 242], ['1273', 242], ['1457', 242], ['0184', 241], ['1485', 241], ['0254', 239], ['0256', 239],
                        ['0568', 239], ['2579', 238], ['3458', 236], ['1349', 233], ['3896', 232], ['2365', 231], ['2538', 231], ['2379', 231], ['0567', 230], ['1238', 230],
                        ['2794', 230], ['0387', 229], ['4679', 229], ['0234', 227], ['0967', 226], ['0289', 225], ['1356', 225], ['2346', 224], ['1376', 223], ['3659', 223],
                        ['5687', 223], ['1249', 221], ['1679', 221], ['0125', 220], ['0315', 218], ['0429', 217], ['2689', 217], ['1378', 216], ['1385', 213], ['0195', 210],
                        ['2678', 210], ['0237', 207], ['2567', 207], ['3678', 206], ['3457', 204], ['2475', 203], ['3694', 203], ['2459', 202], ['0124', 201], ['2465', 201],
                        ['1396', 199], ['3658', 198], ['0139', 196], ['0192', 194], ['0789', 193], ['1568', 191], ['0268', 190], ['4579', 190], ['0259', 188], ['0468', 188],
                        ['0173', 187], ['0136', 184], ['0285', 184], ['0384', 183], ['1578', 183], ['3589', 182], ['0397', 181], ['1593', 181], ['3465', 181], ['2486', 178],
                        ['1278', 176], ['2354', 171], ['1247', 168], ['0168', 167], ['4567', 167], ['1469', 166], ['4698', 163], ['1246', 162], ['0269', 158], ['0637', 157],
                        ['0849', 156], ['4596', 154], ['3495', 151], ['0198', 150], ['2357', 150], ['0358', 148], ['2478', 148], ['0598', 147], ['0578', 141], ['1389', 139],
                        ['0479', 137], ['4789', 134], ['2638', 133], ['5689', 132], ['0649', 131], ['1647', 131], ['1598', 129], ['2738', 128], ['0185', 126], ['1560', 124],
                        ['0174', 123], ['0718', 117], ['0359', 116], ['1275', 116], ['1235', 115], ['0239', 114], ['0123', 112], ['0183', 112], ['0487', 111], ['0238', 109],
                        ['0354', 109], ['1263', 109], ['1498', 106], ['0396', 105], ['1259', 105], ['0196', 103], ['2859', 94], ['0698', 93], ['2639', 90], ['1256', 89],
                        ['1576', 87], ['1456', 84], ['1357', 83], ['0246', 82], ['2586', 81], ['1794', 71], ['0127', 66], ['0278', 59], ['1784', 59], ['3674', 34]]

i12_winnings = [['0056', 1015], ['1494', 910], ['3384', 785], ['0299', 706], ['0114', 702], ['0072', 684], ['4699', 636], ['0047', 607], ['4559', 593], ['0089', 592],
                        ['1224', 577], ['0013', 563], ['6697', 556], ['2447', 543], ['2247', 538], ['1334', 503], ['1882', 500], ['0042', 498], ['1128', 497], ['1129', 493],
                        ['2268', 489], ['2275', 488], ['7697', 488], ['0021', 483], ['1699', 477], ['4047', 473], ['0338', 467], ['2344', 463], ['3356', 445], ['6878', 430],
                        ['0094', 418], ['0669', 418], ['4799', 416], ['1016', 415], ['1299', 413], ['4456', 412], ['0035', 410], ['1337', 410], ['2779', 405], ['4478', 401],
                        ['1134', 400], ['1148', 398], ['0499', 393], ['1377', 393], ['3688', 391], ['0331', 388], ['0889', 388], ['3677', 381], ['4899', 379], ['1139', 378],
                        ['1383', 375], ['2234', 373], ['2296', 373], ['3595', 371], ['1665', 369], ['1747', 363], ['2256', 359], ['2556', 359], ['1778', 358], ['0727', 356],
                        ['2466', 356], ['4668', 355], ['2799', 354], ['0171', 353], ['2339', 353], ['0026', 352], ['1565', 349], ['1136', 348], ['0115', 346], ['4757', 346],
                        ['4669', 344], ['0118', 341], ['1434', 341], ['2696', 341], ['1622', 340], ['4599', 338], ['0337', 336], ['7969', 336], ['2289', 334], ['5795', 333],
                        ['3797', 332], ['1585', 331], ['3866', 331], ['6898', 329], ['0046', 328], ['2334', 328], ['0336', 326], ['4667', 326], ['0366', 324], ['0448', 324],
                        ['2246', 322], ['0058', 321], ['2088', 321], ['1595', 321], ['4688', 321], ['2237', 319], ['0076', 318], ['4479', 316], ['3378', 314], ['1164', 311],
                        ['2259', 311], ['3347', 310], ['0177', 309], ['2337', 309], ['2477', 309], ['2248', 306], ['0545', 304], ['3788', 299], ['5578', 299], ['2278', 296],
                        ['0668', 295], ['0558', 294], ['1126', 294], ['2388', 294], ['0466', 293], ['3435', 291], ['0037', 289], ['0737', 284], ['2249', 284], ['2949', 284],
                        ['3537', 284], ['4557', 284], ['1223', 278], ['0553', 275], ['3305', 274], ['2627', 274], ['3389', 274], ['4588', 274], ['5586', 271], ['0025', 269],
                        ['1474', 269], ['3889', 269], ['1217', 264], ['1252', 259], ['5778', 259], ['0034', 258], ['0068', 258], ['0051', 256], ['0588', 254], ['1788', 254],
                        ['2235', 251], ['4674', 249], ['2788', 246], ['2729', 241], ['4818', 239], ['3436', 239], ['6896', 239], ['3235', 236], ['3494', 231], ['1636', 226],
                        ['1167', 224], ['0232', 223], ['0969', 223], ['1138', 222], ['1125', 216], ['5569', 216], ['4457', 214], ['2633', 211], ['3556', 211], ['2566', 209],
                        ['3359', 204], ['3669', 201], ['1868', 196], ['3447', 194], ['3309', 189], ['0788', 189], ['1189', 189], ['1277', 187], ['1228', 186], ['1557', 184],
                        ['1668', 184], ['2425', 184], ['3455', 184], ['0014', 181], ['0081', 181], ['0166', 179], ['1455', 179], ['3397', 179], ['4468', 179], ['4776', 176],
                        ['0091', 175], ['0494', 175], ['0155', 174], ['1123', 174], ['1168', 174], ['1336', 174], ['1499', 174], ['2464', 174], ['4485', 172], ['0477', 171],
                        ['5859', 171], ['6267', 169], ['3979', 169], ['1646', 167], ['2258', 167], ['0029', 164], ['2969', 164], ['7378', 164], ['2773', 161], ['0755', 160],
                        ['1335', 160], ['1588', 160], ['0599', 159], ['1775', 159], ['2868', 159], ['0016', 157], ['0028', 157], ['0776', 157], ['2944', 157], ['3558', 157],
                        ['0107', 156], ['0036', 155], ['7789', 155], ['0225', 154], ['0199', 152], ['0228', 152], ['1233', 150], ['0989', 149], ['4115', 149], ['1229', 149],
                        ['3396', 149], ['0595', 147], ['0799', 145], ['1518', 145], ['0464', 144], ['1196', 144], ['4946', 144], ['0233', 142], ['0399', 142], ['5979', 142],
                        ['5660', 139], ['1797', 139], ['5788', 137], ['0144', 135], ['1159', 135], ['0552', 134], ['5669', 134], ['0787', 132], ['1165', 132], ['2545', 130],
                        ['7898', 130], ['1244', 127], ['1883', 127], ['4787', 127], ['0838', 125], ['3454', 125], ['2066', 124], ['6678', 124], ['1399', 122], ['1157', 120],
                        ['5458', 120], ['3358', 119], ['0212', 117], ['1741', 114], ['0779', 112], ['4459', 112], ['5996', 112], ['0032', 110], ['0292', 110], ['1137', 110],
                        ['2848', 110], ['2239', 107], ['2454', 107], ['0057', 105], ['0119', 105], ['1227', 105], ['1266', 105], ['1599', 105], ['2588', 105], ['3376', 105],
                        ['0038', 102], ['2238', 102], ['2338', 102], ['2757', 102], ['6576', 102], ['0096', 100], ['0344', 100], ['0667', 100], ['6899', 100], ['0709', 97],
                        ['2668', 97], ['3699', 97], ['4889', 97], ['0093', 95], ['0445', 95], ['1142', 95], ['1153', 95], ['3299', 95], ['2778', 95], ['4498', 95],
                        ['0059', 92], ['2557', 92], ['1355', 90], ['2355', 90], ['2558', 90], ['3667', 90], ['4878', 90], ['5567', 90], ['4993', 85], ['4556', 85],
                        ['4566', 85], ['5899', 85], ['2889', 82], ['3665', 82], ['5677', 82], ['0084', 80], ['0655', 80], ['5529', 80], ['2995', 80], ['3488', 80],
                        ['5688', 80], ['1339', 75], ['3448', 75], ['0226', 72], ['3599', 72], ['1255', 70], ['2998', 70], ['3464', 70], ['5668', 70], ['5889', 70],
                        ['0757', 65], ['1197', 65], ['1844', 65], ['2236', 65], ['3577', 65], ['0054', 62], ['3034', 60], ['6808', 60], ['1899', 60], ['2448', 60],
                        ['3368', 60], ['3477', 60], ['6787', 60], ['7899', 60], ['1013', 55], ['0224', 55], ['0424', 55], ['2636', 55], ['4366', 55], ['1187', 52],
                        ['0078', 50], ['0272', 50], ['1194', 50], ['1464', 50], ['2677', 50], ['8993', 50], ['4779', 50], ['1677', 45], ['7919', 45], ['3885', 45],
                        ['0881', 40], ['6167', 40], ['1966', 40], ['1012', 35], ['4088', 30], ['3394', 30], ['5537', 30], ['4514', 25], ['8891', 25], ['5797', 25]]

i24_all24m_num_winning = [['1285', 269], ['1638', 237], ['0154', 229], ['4601', 226], ['3478', 222],
                          ['3429', 218], ['2697', 216], ['2758', 210], ['7608', 210], ['1648', 171],
                          ['5824', 168], ['0126', 166], ['5697', 166], ['0451', 166], ['3184', 158],
                          ['8697', 155], ['3089', 155], ['5329', 155], ['2597', 153], ['1940', 150],
                          ['4683', 150], ['1043', 147], ['0164', 146], ['0791', 143], ['2674', 140],
                          ['0357', 138], ['5640', 137], ['3049', 137], ['1743', 137], ['1356', 137],
                          ['4810', 134], ['6749', 134], ['6097', 133], ['3948', 132], ['1892', 132],
                          ['9254', 129], ['7598', 129], ['0182', 127], ['1792', 127], ['6375', 126],
                          ['7486', 126], ['0879', 124], ['4863', 124], ['7892', 124], ['7891', 124],
                          ['2675', 122], ['2986', 121], ['2143', 121], ['3847', 121], ['6705', 121],
                          ['1786', 121], ['1208', 121], ['2785', 121], ['3694', 120], ['5962', 119],
                          ['1379', 116], ['0284', 116], ['4283', 116], ['2168', 116], ['4518', 116],
                          ['6237', 116], ['0475', 116], ['7826', 116], ['0463', 116], ['7458', 116],
                          ['9720', 116], ['1846', 116], ['2947', 116], ['1689', 116], ['5026', 116],
                          ['1869', 116], ['2649', 116], ['5419', 116], ['1402', 116], ['3967', 116],
                          ['4508', 116], ['3086', 116], ['0569', 116], ['4258', 114], ['4893', 114],
                          ['8369', 114], ['1760', 113], ['7536', 113], ['3680', 113], ['2167', 113],
                          ['1034', 113], ['1734', 113], ['1593', 113], ['3105', 113], ['0746', 113],
                          ['0914', 113], ['9137', 113], ['0762', 113], ['6034', 113], ['2839', 113],
                          ['0493', 113], ['2809', 113], ['4705', 113], ['2473', 113], ['8173', 113],
                          ['2451', 111], ['3695', 111], ['3685', 111], ['5864', 111], ['5861', 111],
                          ['4358', 111], ['2395', 111], ['3947', 111], ['3625', 111], ['2381', 111],
                          ['4739', 108], ['1754', 108], ['0726', 108], ['7329', 108], ['7062', 108],
                          ['8157', 108], ['4631', 108], ['2194', 108], ['0517', 108], ['7839', 108],
                          ['6187', 108], ['8736', 108], ['1926', 108], ['1059', 108], ['3592', 108],
                          ['5036', 108], ['5971', 108], ['2367', 108], ['1097', 108], ['6847', 108],
                          ['3712', 108], ['0149', 108], ['7091', 108], ['0723', 105], ['2053', 105],
                          ['9753', 105], ['0527', 105], ['4635', 105], ['7205', 105], ['6427', 105],
                          ['4298', 105], ['2984', 105], ['0473', 105], ['7425', 105], ['7954', 105],
                          ['2408', 105], ['1956', 105]]


i12_all24m_num_winning = [['2099', 527], ['2119', 438], ['0560', 428], ['0072', 360], ['1303', 323],
                          ['5633', 313], ['4699', 308], ['4766', 296], ['0988', 293], ['3318', 293],
                          ['4595', 293], ['2077', 281], ['4688', 271], ['5951', 266], ['1929', 264],
                          ['2289', 259], ['6228', 256], ['2433', 256], ['3114', 256], ['2088', 251],
                          ['5658', 251], ['6642', 251], ['1242', 251], ['5587', 249], ['2247', 249],
                          ['6838', 249], ['0448', 244], ['6988', 244], ['7729', 244], ['4110', 244],
                          ['0031', 244], ['8548', 239], ['0508', 239], ['9279', 239], ['4047', 234],
                          ['3436', 234], ['6946', 234], ['9414', 229], ['6773', 229], ['3537', 229],
                          ['0098', 229], ['1585', 229], ['1443', 229], ['0118', 229], ['0102', 229],
                          ['2742', 229], ['6926', 229], ['0703', 229], ['4818', 224], ['8949', 224],
                          ['1373', 224], ['3834', 224], ['6967', 224], ['9967', 224], ['9767', 224],
                          ['3305', 224], ['7147', 224], ['5060', 224], ['5722', 224], ['0120', 224],
                          ['4427', 224], ['4757', 224], ['5359', 224], ['0177', 224], ['4331', 224],
                          ['4456', 224], ['6033', 224], ['1882', 224], ['9479', 224], ['4491', 224],
                          ['0737', 224], ['5334', 224], ['8550', 224], ['0205', 219], ['0470', 219],
                          ['6744', 219], ['3384', 219], ['2124', 219], ['2327', 219], ['0046', 219],
                          ['2040', 214], ['5405', 214], ['1140', 214], ['7688', 214], ['5475', 214],
                          ['4727', 214], ['4149', 214], ['2125', 214], ['1300', 214], ['2287', 214],
                          ['9409', 214], ['3050', 214], ['1316', 214], ['7731', 214], ['7976', 214],
                          ['5778', 214], ['4101', 214], ['9113', 214], ['9866', 214], ['2926', 214],
                          ['4811', 209], ['9323', 209], ['8832', 209], ['4599', 209], ['2275', 209],
                          ['4822', 209], ['9755', 209], ['8717', 209], ['1107', 209], ['6227', 209],
                          ['3224', 209], ['7338', 209], ['8850', 209], ['0511', 209], ['4742', 209],
                          ['4714', 209], ['9422', 209], ['1126', 209], ['3803', 209], ['9946', 209],
                          ['4611', 209], ['0650', 209], ['0094', 209], ['0407', 209], ['2526', 209],
                          ['1821', 209], ['9008', 209], ['9924', 209], ['8893', 209], ['0076', 209],
                          ['2007', 209], ['1699', 209], ['1271', 209], ['0696', 209], ['2592', 209],
                          ['1878', 209], ['4847', 209], ['5561', 209], ['7323', 209], ['4324', 209],
                          ['1334', 209], ['2344', 209], ['6101', 209], ['3703', 209], ['8378', 209],
                          ['4470', 209], ['8812', 209], ['0042', 209], ['6683', 209], ['1494', 188],
                          ['4373', 173], ['6242', 168], ['8334', 168], ['6878', 156], ['4546', 136],
                          ['7047', 131], ['7288', 131], ['9227', 129], ['1007', 126], ['1228', 126],
                          ['7494', 126], ['6648', 126], ['0014', 126], ['0338', 119], ['1061', 119],
                          ['2243', 119], ['2162', 119], ['5626', 114], ['1148', 114], ['6229', 114],
                          ['1557', 114], ['6181', 114], ['3797', 114], ['0788', 114], ['6267', 114],
                          ['9908', 114], ['3447', 114], ['2268', 109], ['3772', 104], ['3839', 104],
                          ['5503', 104], ['2425', 104], ['3532', 104], ['6769', 104], ['1922', 104],
                          ['7939', 104], ['0305', 104], ['5015', 104], ['6065', 104], ['0105', 104],
                          ['6442', 104], ['4934', 104], ['7738', 104], ['4115', 104], ['3550', 104],
                          ['4070', 104], ['3539', 99], ['6976', 99], ['5536', 99], ['2302', 99],
                          ['0663', 99], ['0646', 99], ['1128', 99], ['8466', 99], ['4776', 99],
                          ['1132', 99], ['1996', 99], ['9906', 99], ['3040', 99], ['5562', 99],
                          ['0034', 99], ['6494', 99], ['6499', 99], ['1299', 99], ['8009', 99],
                          ['4475', 97], ['7141', 94], ['2550', 94], ['6188', 92], ['1993', 92],
                          ['3118', 92], ['4439', 92], ['1858', 90], ['2862', 89], ['8010', 89],
                          ['2052', 89], ['3693', 89], ['9330', 89], ['7668', 89], ['3326', 89],
                          ['6168', 89], ['1622', 89], ['1232', 89], ['0409', 89], ['7793', 89],
                          ['9549', 89], ['4559', 89], ['3843', 89], ['0171', 89], ['2565', 89],
                          ['3966', 89], ['5795', 89], ['7393', 89], ['2321', 89], ['8559', 89],
                          ['8826', 89], ['4775', 87], ['1139', 87], ['7127', 87], ['5451', 84],
                          ['0995', 84], ['0668', 84]]
#i24_all24m_num_winning = 147 num
#i12_all24m_num_winning = 252 num
num = []
for each in i24_winnings[:180]:
    num.append(each[0])
for each in i12_winnings[:240]:
    num.append(each[0])
winning = analyze_num_bought(num)


print winning[0]
