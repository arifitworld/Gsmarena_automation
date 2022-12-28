from requests import post
def featureimg(img_src,phone_name):
    '''
    :param img_src: enter image url
    :param phone_name: and the image url
    :return: it will give you a wordpress gutenberg fromatted code.
    '''
    code = f'<!-- wp:image {{"align":"center","width":160,"height":212,"sizeSlug":"large"}} --><figure class="wp-block-image aligncenter size-large is-resized"><img src="{img_src}" alt="" width="160" height="212"/><figcaption class="wp-element-caption">{phone_name}</figcaption></figure><!-- /wp:image -->'
    return code

def paragraph(text):
    '''
    :param text: enter your text
    :return: It will return you  gutenberg fromatted paragraph code.
    '''
    code = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return code

def urlify(phone_name):
    '''
    :param phone_name: enter the phone name
    :return: then the urlify function giue you a url
    '''
    code = f'{phone_name}'
    url = code.strip().lower().replace(' ','-')
    return url

def heading2(text):
    '''
    :param text: Enter the title text
    :return: it will return gutenberg H2 tag.
    '''
    code = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return code

def wptable(dictionary):
    '''
    :param dictionary: add your dictionary
    :return: this function wiil give you wp table data
    '''
    start_code = '<!-- wp:table --><figure class="wp-block-table"><table><tbody>'
    for key, value in dictionary.items():
        tr_data = f'<tr><td>{key}</td><td>{value}</td></tr>'
        start_code += tr_data
    start_code += '</tbody></table></figure><!-- /wp:table -->'
    return start_code


