# scrapy_crx

## Description

- 这个项目是要爬取一个NIH数据集的标签，由于图片我已经爬取好了，这里我就只爬取标签。后续我会把下载图片链接的功能增加进来。
- 环境如下：PyCharm + Python3.5（Anaconda）+ Scrapy1.5

## API接口

API接口的格式如下：

~~~json
{
   "min": 1,
   "max": 2,
   "count": 2,
   "total": 7470,
   "approximage": "false",
   "list":    [
            {
         "uid": "CXR1",
         "pmcid": "1",
         "note": "The data are drawn from multiple hospital systems.",
         "docSource": "CXR",
         "articleType": "rr",
         "title": "Indiana University Chest X-ray Collection",
         "fulltext_html_url": "",
         "journal_title": "",
         "journal_abbr": "",
         "journal_date":          {
            "day": "01",
            "month": "08",
            "year": "2013"
         },
         "authors": "Kohli MD, Rosenman M",
         "affiliate": "Indiana University",
         "impression": "Normal chest x-XXXX.",
         "MeSH":          {
            "minor": [],
            "major": ["normal"]
         },
         "Problems": "normal",
         "ccLicense": "byncnd",
         "licenseURL": "http://creativecommons.org/licenses/by-nc-nd/4.0/",
         "licenseType": "open-access",
         "abstract": "<p><b>Comparison: <\/b>None.<\/p><p><b>Indication: <\/b>Positive TB test<\/p><p><b>Findings: <\/b>The cardiac silhouette and mediastinum size are within normal limits. There is no pulmonary edema. There is no focal consolidation. There are no XXXX of a pleural effusion. There is no evidence of pneumothorax.<\/p><p><b>Impression: <\/b>Normal chest x-XXXX.<\/p>",
         "image":          {
            "id": "F1",
            "caption": "Xray Chest PA and Lateral",
            "modalityMajor": "x",
            "mention": ""
         },
         "imgThumb": "/imgs/100/1/1/CXR1_1_IM-0001-3001.png",
         "imgLarge": "/imgs/512/1/1/CXR1_1_IM-0001-3001.png",
         "imgThumbLarge": "/imgs/137/1/1/CXR1_1_IM-0001-3001.png",
         "imgGrid150": "/imgs/150/1/1/CXR1_1_IM-0001-3001.png",
         "similarInCollection": "retrieve.php?simCollection=CXR1_1_IM-0001-3001&query=&req=3",
         "getArticleFigures": "retrieve.php?uid=CXR1&req=5",
         "detailedQueryURL": "retrieve.php?img=CXR1_1_IM-0001-3001&query=&coll=cxr&req=4",
         "similarInResults": "retrieve.php?simResults=CXR1_1_IM-0001-3001&query=&coll=cxr&req=2"
      },
            {
         "uid": "CXR1",
         "pmcid": "1",
         "note": "The data are drawn from multiple hospital systems.",
         "docSource": "CXR",
         "articleType": "rr",
         "title": "Indiana University Chest X-ray Collection",
         "fulltext_html_url": "",
         "journal_title": "",
         "journal_abbr": "",
         "journal_date":          {
            "day": "01",
            "month": "08",
            "year": "2013"
         },
         "authors": "Kohli MD, Rosenman M",
         "affiliate": "Indiana University",
         "impression": "Normal chest x-XXXX.",
         "MeSH":          {
            "minor": [],
            "major": ["normal"]
         },
         "Problems": "normal",
         "ccLicense": "byncnd",
         "licenseURL": "http://creativecommons.org/licenses/by-nc-nd/4.0/",
         "licenseType": "open-access",
         "abstract": "<p><b>Comparison: <\/b>None.<\/p><p><b>Indication: <\/b>Positive TB test<\/p><p><b>Findings: <\/b>The cardiac silhouette and mediastinum size are within normal limits. There is no pulmonary edema. There is no focal consolidation. There are no XXXX of a pleural effusion. There is no evidence of pneumothorax.<\/p><p><b>Impression: <\/b>Normal chest x-XXXX.<\/p>",
         "image":          {
            "id": "F2",
            "caption": "Xray Chest PA and Lateral",
            "modalityMajor": "x",
            "mention": ""
         },
         "imgThumb": "/imgs/100/1/1/CXR1_1_IM-0001-4001.png",
         "imgLarge": "/imgs/512/1/1/CXR1_1_IM-0001-4001.png",
         "imgThumbLarge": "/imgs/137/1/1/CXR1_1_IM-0001-4001.png",
         "imgGrid150": "/imgs/150/1/1/CXR1_1_IM-0001-4001.png",
         "similarInCollection": "retrieve.php?simCollection=CXR1_1_IM-0001-4001&query=&req=3",
         "getArticleFigures": "retrieve.php?uid=CXR1&req=5",
         "detailedQueryURL": "retrieve.php?img=CXR1_1_IM-0001-4001&query=&coll=cxr&req=4",
         "similarInResults": "retrieve.php?simResults=CXR1_1_IM-0001-4001&query=&coll=cxr&req=2"
      }
   ]
}

~~~

可以看到，我们需要的是 list 里的 “problems”，和  “imgLarge” 两个字段，其中 imgLarge 可以通过路径解析出文件名。

具体的实现请参照代码。

