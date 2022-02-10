# Remaining BE Champions

[![License][license-image]][license-url]

Calculates the BE (blue essence) required to buy all unowned champions in League Of Legends using Riot LCU api.

The script gets the list of owned champions, the champion shards in the loot as well as the prices to buy champions from the store. it prioritizes buying champions using shards but if there's none then the store price is used.

## Installing Dependencies

```bash
py -3.7 -m venv venv
venv/Scripts/pip install install -r requirements.txt
```

## Usage

> Please make sure the client is open for the script to work.

```bash
venv/Scripts/python -m remaining-be-champions
```

### Example Output

```text
Name            ID      Store Price     Loot Price
Shyvana          102     3150            1890
Ahri             103     3150            None
Fizz             105     4800            None
Rengar           107     4800            None
Varus            110     4800            2880
Viktor           112     4800            None
Sejuani          113     4800            2880
Ziggs            115     4800            None
...
Skarner          72      4800            2880
Heimerdinger             74      3150            1890
Nidalee          76      3150            1890
Gragas           79      3150            1890
Ezreal           81      3150            None
Lillia           876     6300            None
Gwen             887     6300            None
Malzahar                 90      4800            None
Kog'Maw          96      4800            None
------------------------------------------------------------------
Total Price Without Loot:        217,350
Total Price:                     174,870
Champions To Buy:                45
```

## Tools Used

* [Visual Studio Code](https://code.visualstudio.com/)
* [LCU API documentation](http://www.mingweisamuel.com/lcu-schema/tool/#//)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

[license-image]: https://img.shields.io/badge/License-MIT-brightgreen.svg
[license-url]: https://opensource.org/licenses/MIT
