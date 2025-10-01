# Bambu Lab RFID Library

This repository contains a collection of RFID tag scans from Bambu Lab filament spools. The data can be used to create cloned tags for Bambu Lab printers or for research purposes.

For more information about Bambu Lab RFID tags and their format, see https://github.com/queengooborg/Bambu-Lab-RFID-Tag-Guide.

## Viewing Tag Data

A script is included in this repository, `parse.py`, that will parse a tag dump and extract its information in an easy-to-read terminal output and easy-to-parse JSON format.  To run it, simply run `python3 parse.py [/path/to/tag.bin-or-json]`.

## Contributing

The best way to contribute is to provide data for Bambu Lab RFID tags. Not sure how to obtain the data? Check out the [guide written in the Bambu Lab RFID Tag Guide repository](https://github.com/queengooborg/Bambu-Lab-RFID-Tag-Guide/blob/main/docs/ReadTags.md)!

Tags are stored in the following folder structure: `Material Category` > `Material Name` > `Color Name` > `Tag UID` > `Tag Files`

## List of Bambu Lab Materials + Colors

Status Icon Legend:

- ✅: Have tag data
- ❌: No tag scanned
- ⚠️: See notes
- 🔨: Testing
- ⏳: Tag data is for an older version of material

### 3DE Premium PLA Openspool
| Color                          | Filament Code | Variant ID | Status |
| -------------------------------| ------------- | ---------- | ------ |
| Aqua Blue                       | 3000          | A50-P0     | 🔨     |
| Army Green                      | 3001          | A50-P1     | 🔨     |
| Blue                            | 3002          | A50-P2     | 🔨     |
| Brown                           | 3003          | A50-P3     | 🔨     |
| Camel Beige                     | 3004          | A50-P4     | 🔨     |
| Cherry Red                      | 3005          | A50-P5     | 🔨     |
| Chocolate Brown                 | 3006          | A50-P6     | 🔨     |
| Cold White                      | 3007          | A50-P7     | 🔨     |
| Cool Grey                       | 3008          | A50-P8     | 🔨     |
| Dark Blue                       | 3009          | A50-P9     | 🔨     |
| Dark Stone                      | 3010          | A50-P10    | 🔨     |
| Dino Green                      | 3011          | A50-P11    | 🔨     |
| Flame Orange                    | 3012          | A50-P12    | 🔨     |
| Gecko Green                     | 3013          | A50-P13    | 🔨     |
| Ghost White                     | 3014          | A50-P14    | 🔨     |
| Hot Pink                        | 3015          | A50-P15    | 🔨     |
| Lavender Purple                 | 3016          | A50-P16    | 🔨     |
| Leaf Green                      | 3017          | A50-P17    | 🔨     |
| Leather Brown                   | 3018          | A50-P18    | 🔨     |
| Light Stone                     | 3019          | A50-P19    | 🔨     |
| Magenta                         | 3020          | A50-P20    | 🔨     |
| Mailbox Red                     | 3021          | A50-P21    | 🔨     |
| Marine Blue                     | 3022          | A50-P22    | 🔨     |
| Midnight Black                  | 3023          | A50-P23    | 🔨     |
| Moss Green                      | 3024          | A50-P24    | 🔨     |
| Mystic Blue                     | 3025          | A50-P25    | 🔨     |
| Neon Yellow                     | 3026          | A50-P26    | 🔨     |
| Normal Blue                     | 3027          | A50-P27    | 🔨     |
| Nuclear Green                   | 3028          | A50-P28    | 🔨     |
| Nude Color                      | 3029          | A50-P29    | 🔨     |
| Pearl Copper                    | 3030          | A50-P30    | 🔨     |
| Pearl Nature                    | 3031          | A50-P31    | 🔨     |
| Pearl Purplish Red              | 3032          | A50-P32    | 🔨     |
| Pearl Red Brown                 | 3033          | A50-P33    | 🔨     |
| Pink                            | 3034          | A50-P34    | 🔨     |
| Pirate Black                    | 3035          | A50-P35    | 🔨     |
| Purple                          | 3036          | A50-P36    | 🔨     |
| Ruby Red                        | 3037          | A50-P37    | 🔨     |
| Safety Orange                   | 3038          | A50-P38    | 🔨     |
| Signal Yellow                   | 3039          | A50-P39    | 🔨     |
| Slate Grey                      | 3040          | A50-P40    | 🔨     |
| Snow White                      | 3041          | A50-P41    | 🔨     |
| Steel Blue                      | 3042          | A50-P42    | 🔨     |
| Sun Yellow                      | 3043          | A50-P43    | 🔨     |
| Sunrise Yellow                  | 3044          | A50-P44    | 🔨     |
| Terminator Grey                 | 3045          | A50-P45    | 🔨     |
| Transparent Black               | 3046          | A50-P46    | 🔨     |
| Transparent Blue                | 3047          | A50-P47    | 🔨     |
| Transparent color 302hk         | 3048          | A50-P48    | 🔨     |
| Transparent Green               | 3049          | A50-P49    | 🔨     |
| Transparent Light Grey          | 3050          | A50-P50    | 🔨     |
| Transparent Orange              | 3051          | A50-P51    | 🔨     |
| Transparent Red                 | 3052          | A50-P52    | 🔨     |
| Transparent Yellow              | 3053          | A50-P53    | 🔨     |
| Unicorn Pink                    | 3054          | A50-P54    | 🔨     |
| Water Blue                      | 3055          | A50-P55    | 🔨     |

### 3DE Premium PLA 
| Color                          | Filament Code | Variant ID | Status |
| -------------------------------| ------------- | ---------- | ------ |
| Aqua Blue                       | 3000          | A50-P0     | ❌     |
| Army Green                      | 3001          | A50-P1     | ❌     |
| Blue                            | 3002          | A50-P2     | ❌     |
| Brown                           | 3003          | A50-P3     | ❌     |
| Camel Beige                     | 3004          | A50-P4     | ❌     |
| Cherry Red                      | 3005          | A50-P5     | ❌     |
| Chocolate Brown                 | 3006          | A50-P6     | ❌     |
| Cold White                      | 3007          | A50-P7     | ❌     |
| Cool Grey                       | 3008          | A50-P8     | ❌     |
| Dark Blue                       | 3009          | A50-P9     | ❌     |
| Dark Stone                      | 3010          | A50-P10    | ❌     |
| Dino Green                      | 3011          | A50-P11    | ❌     |
| Flame Orange                    | 3012          | A50-P12    | ❌     |
| Gecko Green                     | 3013          | A50-P13    | ❌     |
| Ghost White                     | 3014          | A50-P14    | ❌     |
| Hot Pink                        | 3015          | A50-P15    | ❌     |
| Lavender Purple                 | 3016          | A50-P16    | ❌     |
| Leaf Green                      | 3017          | A50-P17    | ❌     |
| Leather Brown                   | 3018          | A50-P18    | ❌     |
| Light Stone                     | 3019          | A50-P19    | ❌     |
| Magenta                         | 3020          | A50-P20    | ❌     |
| Mailbox Red                     | 3021          | A50-P21    | ❌     |
| Marine Blue                     | 3022          | A50-P22    | ❌     |
| Midnight Black                  | 3023          | A50-P23    | ❌     |
| Moss Green                      | 3024          | A50-P24    | ❌     |
| Mystic Blue                     | 3025          | A50-P25    | ❌     |
| Neon Yellow                     | 3026          | A50-P26    | ❌     |
| Normal Blue                     | 3027          | A50-P27    | ❌     |
| Nuclear Green                   | 3028          | A50-P28    | ❌     |
| Nude Color                      | 3029          | A50-P29    | ❌     |
| Pearl Copper                    | 3030          | A50-P30    | ❌     |
| Pearl Nature                    | 3031          | A50-P31    | ❌     |
| Pearl Purplish Red              | 3032          | A50-P32    | ❌     |
| Pearl Red Brown                 | 3033          | A50-P33    | ❌     |
| Pink                            | 3034          | A50-P34    | ❌     |
| Pirate Black                    | 3035          | A50-P35    | ❌     |
| Purple                          | 3036          | A50-P36    | ❌     |
| Ruby Red                        | 3037          | A50-P37    | ❌     |
| Safety Orange                   | 3038          | A50-P38    | ❌     |
| Signal Yellow                   | 3039          | A50-P39    | ❌     |
| Slate Grey                      | 3040          | A50-P40    | ❌     |
| Snow White                      | 3041          | A50-P41    | ❌     |
| Steel Blue                      | 3042          | A50-P42    | ❌     |
| Sun Yellow                      | 3043          | A50-P43    | ❌     |
| Sunrise Yellow                  | 3044          | A50-P44    | ❌     |
| Terminator Grey                 | 3045          | A50-P45    | ❌     |
| Transparent Black               | 3046          | A50-P46    | ❌     |
| Transparent Blue                | 3047          | A50-P47    | ❌     |
| Transparent color 302hk         | 3048          | A50-P48    | ❌     |
| Transparent Green               | 3049          | A50-P49    | ❌     |
| Transparent Light Grey          | 3050          | A50-P50    | ❌     |
| Transparent Orange              | 3051          | A50-P51    | ❌     |
| Transparent Red                 | 3052          | A50-P52    | ❌     |
| Transparent Yellow              | 3053          | A50-P53    | ❌     |
| Unicorn Pink                    | 3054          | A50-P54    | ❌     |
| Water Blue                      | 3055          | A50-P55    | ❌     |

#### PLA Basic

| Color            | Filament Code | Variant ID | Status |
| ---------------- | ------------- | ---------- | ------ |
| Jade White       | 10100         | A00-W1     | ✅     |
| Beige            | 10201         | A00-P0     | ✅     |
| Light Gray       | 10104         | A00-D2     | ✅     |
| Yellow           | 10400         | A00-Y0     | ✅     |
| Sunflower Yellow | 10402         | A00-Y2     | ✅     |
| Pumpkin Orange   | 10301         | A00-A1     | ✅     |
| Orange           | 10300         | A00-A0     | ✅     |
| Gold             | 10401         | A00-Y4     | ✅     |
| Bright Green     | 10503         | A00-G3     | ✅     |
| Bambu Green      | 10501         | A00-G1     | ✅     |
| Mistletoe Green  | 10502         | A00-G2     | ✅     |
| Pink             | 10203         | A00-A0     | ✅     |
| Hot Pink         | 10204         | A00-R3     | ✅     |
| Magenta          | 10202         | A00-P6     | ✅     |
| Red              | 10200         | A00-R0     | ✅     |
| Maroon Red       | 10205         | A00-R2     | ✅     |
| Purple           | 10700         | A00-P5     | ✅     |
| Indigo Purple    | 10701         | A00-P2     | ✅     |
| Turquoise        | 10605         | A00-B5     | ✅     |
| Cyan             | 10603         | A00-B8     | ✅     |
| Cobalt Blue      | 10604         | A00-B3     | ✅     |
| Blue             | 10601         | A09-B4     | ✅     |
| Brown            | 10800         | A00-N0     | ✅     |
| Cocoa Brown      | 10802         | A00-N1     | ✅     |
| Bronze           | 10801         | A00-Y3     | ✅     |
| Gray             | 10103         | A00-D0     | ✅     |
| Silver           | 10102         | A00-D1     | ✅     |
| Blue Grey        | 10602         | A00-B1     | ✅     |
| Dark Gray        | 10105         | A00-D3     | ✅     |
| Black            | 10101         | A00-K0     | ✅     |

#### PLA Lite

| Color       | Filament Code | Variant ID | Status |
| ----------- | ------------- | ---------- | ------ |
| Black       | 16100         | A18-K0     | ✅     |
| Gray        | 16101         | A18-D0     | ✅     |
| White       | 16103         | A18-W0     | ✅     |
| Red         | 16200         | A18-R0     | ✅     |
| Yellow      | 16400         | A18-Y0     | ✅     |
| Cyan        | 16600         | A18-B0     | ✅     |
| Blue        | 16601         | A18-B1     | ✅     |
| Matte Beige | 16602         | A18-P0     | ✅     |

#### PLA Matte

| Color           | Filament Code | Variant ID | Status |
| --------------- | ------------- | ---------- | ------ |
| Ivory White     | 11100         | A01-W2     | ✅     |
| Bone White      | 11103         | A01-W3     | ✅     |
| Lemon Yellow    | 11400         | A01-Y2     | ✅     |
| Mandarin Orange | 11300         | A01-A2     | ✅     |
| Sakura Pink     | 11201         | A01-P3     | ✅     |
| Lilac Purple    | 11700         | A01-P4     | ✅     |
| Plum            | 11204         | A01-R3     | ✅     |
| Scarlet Red     | 11200         | A01-R1     | ✅     |
| Dark Red        | 11202         | A01-R4     | ✅     |
| Apple Green     | 11502         | A01-G0     | ✅     |
| Grass Green     | 11500         | A01-G1     | ✅     |
| Dark Green      | 11501         | A01-G7     | ✅     |
| Ice Blue        | 11601         | A01-B4     | ✅     |
| Sky Blue        | 11603         | A01-B0     | ✅     |
| Marine Blue     | 11600         | A01-B3     | ✅     |
| Dark Blue       | 11602         | A01-B6     | ✅     |
| Desert Tan      | 11401         | A01-Y3     | ✅     |
| Latte Brown     | 11800         | A01-N1     | ✅     |
| Caramel         | 11803         | A01-N3     | ✅     |
| Terracotta      | 11203         | A01-R2     | ✅     |
| Dark Brown      | 11801         | A01-N2     | ✅     |
| Dark Chocolate  | 11802         | A01-N0     | ✅     |
| Ash Grey        | 11102         | A01-D3     | ✅     |
| Nardo Gray      | 11104         | A01-D0     | ✅     |
| Charcoal        | 11101         | A01-K1     | ✅     |

#### PLA Basic Gradient

| Color               | Filament Code | Variant ID | Status |
| ------------------- | ------------- | ---------- | ------ |
| Pink Citrus         | 10903         | A00-M3     | ✅     |
| Dusk Glare          | 10906         | A00-M6     | ✅     |
| Arctic Whisper      | 10900         | A00-M0     | ✅     |
| Solar Breeze        | 10901         | A00-M1     | ✅     |
| Blueberry Bubblegum | 10905         | A00-M5     | ✅     |
| Mint Lime           | 10904         | A00-M4     | ✅     |
| Ocean to Meadow     | 10902         | A00-M2     | ✅     |
| Cotton Candy Cloud  | 10907         | A00-M7     | ✅     |

#### PLA Glow

| Color  | Filament Code | Variant ID | Status |
| ------ | ------------- | ---------- | ------ |
| Green  | 15500         | A12-G0     | ✅     |
| Pink   | 15200         | A12-R0     | ✅     |
| Orange | 15300         | A12-A0     | ✅     |
| Yellow | 15400         | A12-Y0     | ✅     |
| Blue   | 15600         | A12-B0     | ✅     |

#### PLA Marble

| Color        | Filament Code | Variant ID | Status |
| ------------ | ------------- | ---------- | ------ |
| Red Granite  | 13201         | A07-R5     | ✅     |
| White Marble | 13103         | A07-D4     | ✅     |

#### PLA Aero

| Color | Filament Code | Variant ID | Status |
| ----- | ------------- | ---------- | ------ |
| White | 14102         | A11-W0     | ✅     |
| Gray  | 14104         | ?          | ❌     |
| Black | 14103         | A11-K0     | ✅     |

#### PLA Sparkle

| Color                | Filament Code | Variant ID | Status |
| -------------------- | ------------- | ---------- | ------ |
| Alpine Green Sparkle | 13501         | A08-G3     | ✅     |
| Slate Gray Sparkle   | 13102         | A08-D5     | ✅     |
| Royal Purple Sparkle | 13700         | A08-B7     | ✅     |
| Crimson Red Sparkle  | 13200         | A08-R2     | ✅     |
| Onyx Black Sparkle   | 13101         | A08-K2     | ✅     |
| Classic Gold Sparkle | 13402         | A08-Y1     | ✅     |

#### PLA Metal

| Color                 | Filament Code | Variant ID | Status |
| --------------------- | ------------- | ---------- | ------ |
| Cobalt Blue Metallic  | 13600         | A02-B2     | ✅     |
| Oxide Green Metallic  | 13500         | ?          | ❌     |
| Iridium Gold Metallic | 13400         | A02-Y1     | ❌     |
| Copper Brown Metallic | 13800         | ?          | ❌     |
| Iron Gray Metallic    | 13100         | A02-D2     | ❌     |

#### PLA Silk+

| Color       | Filament Code | Variant ID      | Status |
| ----------- | ------------- | --------------- | ------ |
| Pink        | 13207         | A06-R2          | ✅     |
| Titan Gray  | 13108         | A06-D0          | ✅     |
| Blue        | 13604         | A06-B1          | ✅     |
| Purple      | 13702         | ? (Old: A05-P5) | ⏳     |
| Candy Red   | 13205         | A06-R0          | ✅     |
| Candy Green | 13506         | A06-G0          | ✅     |
| Rose Gold   | 13206         | A06-R1          | ✅     |
| Baby Blue   | 13603         | A06-B0          | ✅     |
| Mint        | 13507         | A06-G1          | ✅     |
| Champagne   | 13404         | A06-Y0          | ✅     |
| White       | 13110         | A06-W0          | ✅     |
| Silver      | 13109         | A06-D1          | ✅     |
| Gold        | 13405         | A06-Y1          | ✅     |

#### PLA Silk Multi-Color

| Color                      | Filament Code | Variant ID | Status |
| -------------------------- | ------------- | ---------- | ------ |
| Dawn Radiance              | 13912         | A05-M8     | ✅     |
| Aurora Purple              | 13909         | ?          | ❌     |
| South Beach                | 13906         | A05-M1     | ✅     |
| Neon City (Blue-Magenta)   | 13903         | A05-T3     | ✅     |
| Midnight Blaze (Blue-Red)  | 13902         | A05-T2     | ✅     |
| Gilded Rose (Pink-Gold)    | 13901         | A05-T1     | ✅     |
| Blue Hawaii (Blue-Green)   | 13904         | A05-T4     | ✅     |
| Velvet Eclipse (Black-Red) | 13905         | A05-T5     | ✅     |

#### PLA Galaxy

| Color   | Filament Code | Variant ID | Status |
| ------- | ------------- | ---------- | ------ |
| Purple  | 13602         | A15-B0     | ✅     |
| Green   | 13503         | A15-G0     | ✅     |
| Nebulae | 13504         | A15-G1     | ✅     |
| Brown   | 13203         | A15-R0     | ✅     |

#### PLA Wood

| Color         | Filament Code | Variant ID | Status |
| ------------- | ------------- | ---------- | ------ |
| Black Walnut  | 13107         | A16-K0     | ✅     |
| Rosewood      | 13204         | A16-R0     | ✅     |
| Clay Brown    | 13801         | A16-N0     | ✅     |
| Classic Birch | 13505         | A16-G0     | ✅     |
| White Oak     | 13106         | A16-W0     | ✅     |
| Ochre Yellow  | 13403         | A16-Y0     | ✅     |

#### PLA-CF

| Color        | Filament Code | Variant ID | Status |
| ------------ | ------------- | ---------- | ------ |
| Burgundy Red | 14200         | ?          | ❌     |
| Matcha Green | 14500         | ?          | ❌     |
| Lava Gray    | 14101         | A50-D6     | ❌     |
| Jeans Blue   | 14600         | ?          | ❌     |
| Black        | 14100         | A50-K0     | ✅     |
| Royal Blue   | 14601         | A50-B6     | ❌     |
| Iris Purple  | 14700         | ?          | ❌     |

#### PLA Tough+

| Color  | Filament Code | Variant ID | Status |
| ------ | ------------- | ---------- | ------ |
| Yellow | 12401         | ?          | ❌     |
| White  | 12107         | ?          | ❌     |
| Orange | 12301         | ?          | ❌     |
| Gray   | 12105         | ?          | ❌     |
| Silver | 12106         | ?          | ❌     |
| Cyan   | 12601         | ?          | ❌     |
| Black  | 12104         | ?          | ❌     |

### PETG

#### PETG HF

| Color        | Filament Code | Variant ID | Status |
| ------------ | ------------- | ---------- | ------ |
| Red          | 33200         | G02-R0     | ✅     |
| Blue         | 33600         | G02-B0     | ✅     |
| Black        | 33102         | G02-K0     | ✅     |
| White        | 33100         | G02-W0     | ✅     |
| Gray         | 33101         | G02-D0     | ✅     |
| Yellow       | 33400         | G02-Y0     | ✅     |
| Orange       | 33300         | G02-A0     | ✅     |
| Green        | 33500         | G02-G0     | ✅     |
| Forest Green | 33502         | G02-G2     | ✅     |
| Peanut Brown | 33801         | G02-N1     | ✅     |
| Dark Gray    | 33103         | G02-D1     | ✅     |
| Cream        | 33401         | G02-Y1     | ✅     |
| Lime Green   | 33501         | G02-G1     | ✅     |
| Lake Blue    | 33601         | G02-B1     | ✅     |

#### PETG Translucent

| Color                  | Filament Code | Variant ID | Status |
| ---------------------- | ------------- | ---------- | ------ |
| Translucent Teal       | 32501         | G01-G1     | ✅     |
| Translucent Light Blue | 32600         | G01-B0     | ✅     |
| Clear                  | 32101         | G01-C0     | ✅     |
| Translucent Olive      | 32500         | G01-G0     | ✅     |
| Translucent Orange     | 32300         | G01-A0     | ✅     |
| Translucent Purple     | 32700         | G01-P0     | ✅     |
| Translucent Pink       | 32200         | G01-P1     | ✅     |
| Translucent Brown      | 32800         | G01-N0     | ✅     |
| Translucent Gray       | 32100         | G01-D0     | ✅     |

#### PETG-CF

| Color           | Filament Code | Variant ID | Status |
| --------------- | ------------- | ---------- | ------ |
| Indigo Blue     | 31600         | ?          | ❌     |
| Malachite Green | 31500         | ?          | ❌     |
| Titan Gray      | 31101         | ?          | ❌     |
| Brick Red       | 31200         | ?          | ❌     |
| Violet Purple   | 31700         | G50-P7     | ✅     |
| Black           | 31100         | G50-K0     | ✅     |

### ABS

#### ABS

| Color            | Filament Code | Variant ID | Status |
| ---------------- | ------------- | ---------- | ------ |
| Silver           | 40102         | B00-D1     | ✅     |
| Black            | 40101         | B00-K0     | ✅     |
| White            | 40100         | B00-W0     | ✅     |
| Red              | 40200         | B00-R0     | ✅     |
| Bambu Green      | 40500         | B00-G6     | ✅     |
| Orange           | 40300         | B00-A0     | ✅     |
| Navy Blue        | 40602         | B00-B6     | ✅     |
| Tangerine Yellow | 40402         | B00-Y1     | ✅     |
| Blue             | 40600         | B00-B0     | ✅     |
| Olive            | 40502         | B00-G7     | ✅     |
| Azure            | 40601         | B00-B4     | ✅     |

#### ABS-GF

| Color  | Filament Code | Variant ID | Status |
| ------ | ------------- | ---------- | ------ |
| Orange | 41300         | B50-A0     | ✅     |
| Green  | 41500         | B50-G0     | ❌     |
| Red    | 41200         | B50-R0     | ❌     |
| Yellow | 41400         | ?          | ❌     |
| Blue   | 41600         | ?          | ❌     |
| White  | 41100         | B50-W0     | ❌     |
| Gray   | 41102         | ?          | ❌     |
| Black  | 41101         | B50-K0     | ❌     |

### ASA

#### ASA

| Color | Filament Code | Variant ID | Status |
| ----- | ------------- | ---------- | ------ |
| White | 45100         | B01-W0     | ✅     |
| Green | 45500         | ?          | ❌     |
| Black | 45101         | B01-K0     | ✅     |
| Gray  | 45102         | B01-D0     | ✅     |
| Red   | 45200         | ?          | ❌     |
| Blue  | 45600         | ?          | ❌     |

#### ASA Aero

| Color | Filament Code | Variant ID | Status |
| ----- | ------------- | ---------- | ------ |
| White | 46100         | B02-W0     | ✅     |

#### ASA-CF

| Color | Filament Code | Variant ID | Status |
| ----- | ------------- | ---------- | ------ |
| Black | 46101         | ?          | ❌     |

### PC

#### PC

| Color       | Filament Code | Variant ID | Status |
| ----------- | ------------- | ---------- | ------ |
| Transparent | 60103         | ?          | ❌     |
| Clear Black | 60102         | ?          | ❌     |
| Black       | 60101         | C00-K0     | ✅     |
| White       | 60100         | C00-W0     | ✅     |

#### PC FR

| Color | Filament Code | Variant ID | Status |
| ----- | ------------- | ---------- | ------ |
| Black | 63100         | ?          | ❌     |
| White | 63101         | ?          | ❌     |
| Gray  | 63102         | ?          | ❌     |

### TPU

#### TPU for AMS

| Color      | Filament Code | Variant ID | Status |
| ---------- | ------------- | ---------- | ------ |
| Blue       | 53600         | U02-B0     | ✅     |
| Red        | 53200         | ?          | ❌     |
| Yellow     | 53400         | ?          | ❌     |
| Neon Green | 53500         | ?          | ❌     |
| White      | 53100         | ?          | ❌     |
| Gray       | 53102         | U02-D0     | ✅     |
| Black      | 53101         | U02-K0     | ✅     |

### PA

#### PAHT-CF

| Color | Filament Code | Variant ID | Status |
| ----- | ------------- | ---------- | ------ |
| Black | 70100         | N04-K0     | ✅     |

#### PA6-GF

| Color  | Filament Code | Variant ID | Status |
| ------ | ------------- | ---------- | ------ |
| Blue   | 72600         | ?          | ❌     |
| Orange | 72200         | ?          | ❌     |
| Yellow | 72400         | ?          | ❌     |
| Lime   | 72500         | ?          | ❌     |
| Brown  | 72800         | ?          | ❌     |
| White  | 72102         | ?          | ❌     |
| Gray   | 72103         | ?          | ❌     |
| Black  | 72104         | N08-K0     | ✅     |

### Support Material

#### Support for PLA/PETG

| Color  | Filament Code | Variant ID           | Status |
| ------ | ------------- | -------------------- | ------ |
| Nature | 65102         | S02-W0 (Old: S00-W0) | ✅     |
| Black  | 65103         | S05-C0               | ✅     |

#### Support for PLA (New Version)

| Color | Filament Code | Variant ID | Status |
| ----- | ------------- | ---------- | ------ |
| White | 65104         | ?          | ❌     |

#### Support for ABS

| Color | Filament Code | Variant ID | Status |
| ----- | ------------- | ---------- | ------ |
| White | 66100         | S06-W0     | ✅     |

#### Support for PA/PET

| Color | Filament Code | Variant ID | Status |
| ----- | ------------- | ---------- | ------ |
| Green | 65500         | ?          | ❌     |

#### PVA

| Color | Filament Code | Variant ID | Status |
| ----- | ------------- | ---------- | ------ |
| Clear | 66400         | S04-Y0     | ✅     |

## History

When Bambu Lab released the AMS for their 3D printers, it featured an RFID redear which could read RFID tags embedded on their filament spools to automatically update details such as material type, color and amount of remaining filament. However, the RFID tags were read-protected by keys, signed with an RSA2048 signature and structured in a proprietary format, which meant that only Bambu Lab could create these particular RFID tags and they could only be used on Bambu Lab printers. This led to the start of the [Bambu Research Group and a project to reverse engineer the RFID tag format](https://github.com/queengooborg/Bambu-Lab-RFID-Tag-Guide) in order to develop an open standard for all filament manufacturers and printers.

Of course, to research the tag format, a lot of tag data was required. This led to a community effort to scan lots of tags and cross-reference the data with known details about each spool. Eventually, enough of the format was reverse engineered to be able to determine what an open standard would need. But, the tag scanning didn't stop there, as the community realized another benefit to the collection of tags: even though custom tags couldn't be created due to the signing of the data, the data could be _cloned_ onto new tags and used to tell Bambu Lab printers what material and color a spool was, just like Bambu Lab first-party spools.

Originally, the collection of scanned tags was kept private as the research group was not sure if Bambu Lab would react negatively to sniffing data transfers to obtain hidden keys. However, as time progressed and new methods were discovered to obtain tag data, the group slowly opened up the tag collection and made it easier to access, until eventually it became the consensus to create this repository.
