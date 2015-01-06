import csv
import xml.etree.ElementTree as etree

xml_data = '''<GetSingleItemResponse xmlns="urn:ebay:apis:eBLBaseComponents">
  <Timestamp>2012-10-25T03:09:50.817Z</Timestamp>
  <Ack>Success</Ack>
  <Build>E795_CORE_BUNDLED_15430047_R1</Build>
  <Version>795</Version>
  <Item>
     <Description>...</Description>
     <ItemID>330810813385</ItemID>
     <EndTime>2012-10-25T04:32:37.000Z</EndTime>
     <Location>Paypal Prefered</Location>
     <GalleryURL>...</GalleryURL>
     <PictureURL>...</PictureURL>
     <PictureURL>...</PictureURL>
     <PrimaryCategoryID>177</PrimaryCategoryID>
     <PrimaryCategoryName>
     Computers/Tablets &amp; Networking:Laptops &amp; Netbooks:PC Laptops &amp; Netbooks
     </PrimaryCategoryName>
     <BidCount>2</BidCount>
     <ConvertedCurrentPrice currencyID="USD">294.99</ConvertedCurrentPrice>
     <ListingStatus>Active</ListingStatus>
     <TimeLeft>PT1H22M47S</TimeLeft>
     <Title>
     HP Compaq ZD8000 3800Mhz Full Loaded Ready to go, nice unit &amp; super fast Laptop
     </Title>
     <ShippingCostSummary>
     <ShippingServiceCost currencyID="USD">23.99</ShippingServiceCost>
     <ShippingType>Flat</ShippingType>
     <ListedShippingServiceCost currencyID="USD">23.99</ListedShippingServiceCost>
     </ShippingCostSummary>
     <ItemSpecifics>
        <NameValueList>
           <Name>Operating System</Name>
           <Value>Windows XP Professional</Value>
        </NameValueList>
        <NameValueList>
           <Name>Screen Size</Name>
           <Value>17.0</Value>
        </NameValueList>
        <NameValueList>
           <Name>Processor Type</Name>
           <Value>Intel Pentium 4 HT</Value>
        </NameValueList>
     </ItemSpecifics>
     <Country>US</Country>
     <AutoPay>false</AutoPay>
     <ConditionID>2500</ConditionID>
     <ConditionDisplayName>Seller refurbished</ConditionDisplayName>
   </Item>
</GetSingleItemResponse>'''

def bareTag(tag):
    lst = tag.split('}')
    return lst[-1]


element = etree.fromstring(xml_data)
print element.tag
assert bareTag(element.tag) == 'GetSingleItemResponse'
##etree.dump(element)

# Find the Item element.
item = element.find('{urn:ebay:apis:eBLBaseComponents}Item')
##etree.dump(item)

header = []   # init -- future column names

d = {}        # init -- values of the elements

# Element is a list of children.
for e in item:
    if bareTag(e.tag) == 'ItemSpecifics':
        for nv in e:
            assert bareTag(nv.tag) == 'NameValueList'
            # To be robust, rather find the element than index it.
            # The order could be switched in future.
            name = nv.find('{urn:ebay:apis:eBLBaseComponents}Name')
            value = nv.find('{urn:ebay:apis:eBLBaseComponents}Value')

            # Add the prefix for the dictionary key.
            k = 'ItemSpecifics.' + name.text
            v = value.text

            # Add to the dictionary.
            d[k] = v

            # If not in header, append it.
            if k not in header:
                header.append(k)
    else:
        # General information for the item.
        k = bareTag(e.tag)
        v = e.text

        # Add to the dictionary.
        d[k] = v

        # If not in header, append it.
        if k not in header:
            header.append(k)


# Process the dictionary -- show it on the screen.
for k in d:
    print k + ':', d[k]

# Output to the temporary csv
fname_tmp = 'temporary.csv'
with open(fname_tmp, 'wb') as fout:
    writer = csv.writer(fout)

    # Column name from header as a key, None as default value.
    # Replace newlines by spaces (or any better character 
    # for the purpose) and strip the value.
    row = [d.get(k, None).replace('\n', ' ').strip() for k in header]
    writer.writerow(row)


# Now all records were collected. The header contains all column names.
# Generate the final CSV from the header and the temporary csv.
fname_final = 'output.csv'

with open(fname_tmp, 'rb') as fin, \
     open(fname_final, 'wb') as fout:
    reader =csv.reader(fin)
    writer =csv.writer(fout)

    # Write the header first.
    writer.writerow(header)

    # Copy the lines from the temporary.
    for row in reader:
        writer.writerow(row)