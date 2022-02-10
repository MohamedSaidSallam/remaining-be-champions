from lcu_driver import Connector

connector = Connector()


@connector.ready
async def connect(connection):
    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    summonerId = str((await summoner.json())['summonerId'])

    championsRes = await connection.request('get', '/lol-champions/v1/inventories/' + summonerId + '/champions')
    champions = await championsRes.json()

    championsOwnedStatus = {
        item['id']: item['ownership']['owned'] for item in champions}

    lootRes = await connection.request('get', '/lol-loot/v1/player-loot')
    loot = await lootRes.json()

    lootChampionsValue = {}
    for item in loot:
        if item["type"] == "CHAMPION_RENTAL":
            lootChampionsValue[item['storeItemId']
                               ] = item['upgradeEssenceValue']

    storeCatalogRes = await connection.request('get', '/lol-store/v1/catalog')
    storeCatalog = await storeCatalogRes.json()

    totalPrice = 0
    totalPriceWithoutLoot = 0
    championsToBuyCount = 0
    print('Name\t\tID\tStore Price\tLoot Price')
    for item in storeCatalog:

        itemId = item['itemId']
        if item["inventoryType"] == "CHAMPION" and not championsOwnedStatus[itemId]:
            championsToBuyCount += 1
            print(item['localizations'][list(
                item['localizations'].keys())[0]]['name'], end='')
            print('\t\t', itemId, end='')

            itemPrice = None
            for price in item['prices']:
                if price['currency'] == 'IP':
                    itemPrice = price['cost']
                    break
            totalPriceWithoutLoot += itemPrice
            print('\t', itemPrice, end='')
            print('\t\t', lootChampionsValue[itemId]
                  if itemId in lootChampionsValue else None)
            totalPrice += lootChampionsValue[itemId] if itemId in lootChampionsValue else itemPrice

    print('------------------------------------------------------------------')
    print('Total Price Without Loot:\t', '{:,}'.format(totalPriceWithoutLoot))
    print('Total Price:\t\t\t', '{:,}'.format(totalPrice))
    print('Champions To Buy:\t\t', championsToBuyCount)


connector.start()
