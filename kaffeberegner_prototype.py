def kaffeberegner (gram_kaffe):
    gram_vann = round((gram_kaffe*0.016666666)*1000)
    bloom = gram_kaffe*2
    f_round = gram_vann*0.60
    print(f'Til {gram_kaffe}g kaffe, trenger du {gram_vann}g vann.')
    print(f'Til bloom vil du ha {bloom}g vann med vann.')
    print(f'Første runde etter bloom vil ha {f_round}g kaffe i de første 30 sekundene etter bloom')
    print('tilsett derett resten av kaffen litt saktere')

kaffeberegner(24)
