import os
import requests
import fnmatch
import shutil

import lxml.html
from zipfile import ZipFile

from trail import Trails, Trail


urls = [
    'http://www.wandelzoekpagina.nl/wandeling/ankeveense-plassen/11146/',
    'http://www.wandelzoekpagina.nl/wandeling/belmonte/5025/',
    'http://www.wandelzoekpagina.nl/wandeling/beukenburg/9138/',
    'http://www.wandelzoekpagina.nl/wandeling/boerskotten/11855/',
    'http://www.wandelzoekpagina.nl/wandeling/bieslandse-bos/5014/',
    'http://www.wandelzoekpagina.nl/wandeling/de-horsten/6683/',
    'http://www.wandelzoekpagina.nl/wandeling/de-vuursche/6686/',
    'http://www.wandelzoekpagina.nl/wandeling/elburg/11148/',
    'http://www.wandelzoekpagina.nl/wandeling/elsterberg/6687/',
    'http://www.wandelzoekpagina.nl/wandeling/geniedijk/11857/',
    'http://www.wandelzoekpagina.nl/wandeling/heiligenbergerbeek/8246/',
    'http://www.wandelzoekpagina.nl/wandeling/hollandse-kade/5056/',
    'http://www.wandelzoekpagina.nl/wandeling/holterberg/5044/',
    'http://www.wandelzoekpagina.nl/wandeling/hondsrug/8248/',
    'http://www.wandelzoekpagina.nl/wandeling/ijsselvallei/5062/',
    'http://www.wandelzoekpagina.nl/wandeling/kampina/5010/',
    'http://www.wandelzoekpagina.nl/wandeling/kennemerduinen/5034/',
    'http://www.wandelzoekpagina.nl/wandeling/landgoed-groeneveld/5008/',
    'http://www.wandelzoekpagina.nl/wandeling/lange-duinen/7749/',
    'http://www.wandelzoekpagina.nl/wandeling/markelose-berg/9142/',
    'http://www.wandelzoekpagina.nl/wandeling/meijendel/5018/',
    'http://www.wandelzoekpagina.nl/wandeling/meinweg/8249/',
    'http://www.wandelzoekpagina.nl/wandeling/mookerhei/5013/',
    'http://www.wandelzoekpagina.nl/wandeling/naardermeer/5041/',
    'http://www.wandelzoekpagina.nl/wandeling/nijenhuis/5373/',
    'http://www.wandelzoekpagina.nl/wandeling/noord-hollands-duinreservaat/5012/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-amsterdam/12891/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-beerschoten/15613/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-de-bretten/16186/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-de-weelen/15121/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-den-haag/14380/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-drentsche-aa/14381/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-fort-de-roovere/16185/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-hemelse-berg/15614/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-land-van-ravenstein/16184/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-leeuwarden/15123/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-marienwaerdt---linge/12892/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-mastbos/15615/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-park-lingezegen/16183/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-paterswoldsemeer/15616/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-pietersberg/15122/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-rotterdam-maasstad/12893/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-texel/14383/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-vechtdal/12894/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-wezepsche-heide/15124/',
    'http://www.wandelzoekpagina.nl/wandeling/ns-wandeling-woldberg/15617/',
    'http://www.wandelzoekpagina.nl/wandeling/savelsbos/5039/',
    'http://www.wandelzoekpagina.nl/wandeling/strabrechtse-heide/5027/',
    'http://www.wandelzoekpagina.nl/wandeling/utrechtse-heuvelrug/5024/',
    'http://www.wandelzoekpagina.nl/wandeling/veluwezoom/5021/',
    'http://www.wandelzoekpagina.nl/wandeling/vughtse-lunetten/5017/',
    'http://www.wandelzoekpagina.nl/wandeling/warnsborn/10519/',
]


def main():
    gwurls = get_groenewissel_urls()

    for url in gwurls:
        print(url)

    # trails_all = Trails()
    # for url in urls:
    #     trails = download_extract_gpx_wandelzoekpagina(url)
    #     for trail in trails:
    #         trails_all.append(trail)

    # trails_all.to_json('trails_downloaded.json')


def get_groenewissel_urls():
    urls = []
    url_table = 'http://nswandel.nl/GW.html'
    page = requests.get(url_table)
    tree = lxml.html.fromstring(page.content)
    rows = tree.xpath("//tbody/tr")
    counter = 0
    for row in rows:
        counter += 1
        for column in row.iter():
            if column.tag == 'a':
                page_url = 'http://nswandel.nl/' + column.attrib['href']
                print(page_url + ' ' + str(counter) + '/' + str(len(row)))
                urls.append(page_url)
                download_extract_gpx_nswandel(page_url)
    return urls


def download_extract_gpx_wandelzoekpagina(url):
    page = requests.get(url)
    tree = lxml.html.fromstring(page.content)
    name = tree.xpath('//h1')[0].text
    print(name)
    download_button = tree.xpath('//div[@class="knopgps"]')
    if not download_button:
        print('WARNING: No download button found on page, gpx not available')
        return {}

    trails = Trails()
    download_link = download_button[0].getparent()
    if 'href' in download_link.attrib:
        zipurl = download_link.attrib['href']
        extract_zip_file(zipurl, name)


def download_extract_gpx_nswandel(url):
    page = requests.get(url)
    tree = lxml.html.fromstring(page.content)
    fonts = tree.xpath('//font[@color="#000000"]')
    for font in fonts:
        if font.text == 'GPS-track':
            gpxurl_relative = font.getparent().attrib['href']
            gpxurl_absolute = gpxurl_relative.replace('../..', 'http://nswandel.nl')
            filename = gpxurl_relative.replace('../../gpstracks/', '')
            print(gpxurl_absolute)
            print(filename)
            extract_zip_file(gpxurl_absolute, filename)


def extract_zip_file(zipurl, name):
    outdir = 'extract/' + name
    resp = requests.get(zipurl)
    if '.zip' in zipurl:
        print('unzipping')
        tempzip = open("tempfile.zip", "wb")
        tempzip.write(resp.content)
        tempzip.close()
        zf = ZipFile("tempfile.zip")
        zf.extractall(path=outdir)
        zf.close()
        for root, subFolders, filenames in os.walk(outdir):
            for filename in fnmatch.filter(filenames, '*.gpx'):
                print(os.path.join(root, filename))
                shutil.copyfile(os.path.join(root, filename), os.path.join('extract', filename))
    elif '.gpx' in zipurl:
        filename = os.path.join('extract', name + '.gpx')
        print('writing gpx to: ' + filename)
        with open(filename, 'w') as fileout:
            fileout.write(str(resp.content))


if __name__ == "__main__":
    main()