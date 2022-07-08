from search_engine import laptop_search


def parse_laptop_name(prod_name):
    first_space_idx = prod_name.find(' ')
    manufacturer = prod_name[:first_space_idx]
    prod_name = prod_name[first_space_idx+1:]

    # trim last new keyword
    last_space_idx = prod_name.rfind(' ')
    if prod_name[last_space_idx+1:] == "NEW":
        prod_name = prod_name[:-4]

    return manufacturer, prod_name

def parse_laptop_general_info(line):
    first_slash_idx = line.find(' /')
    is2in1 = line[:first_slash_idx]
    line = line[first_slash_idx+12:] # 운영체제(OS): 까지 넘어간다.

    first_slash_idx = line.find(' /')
    osinfo = line[:first_slash_idx]
    line = line[first_slash_idx+3:]

    first_slash_idx = line.find(' /')
    spec_changed = line[:first_slash_idx]
    line = line[first_slash_idx+7:]

    purpose = line[:-2].split(',')
    
    return is2in1, osinfo, spec_changed, purpose


def parse_laptop_display_info(line):
    if line[:4] != "화면정보":
        print("display parse error")
        return
    line = line[5:]
    items = line.split(' /')
    display_size, resolution = items[:2]
    other_spec = items[2:]

    other_spec = [ i.strip() for i in other_spec if i ]
    display_info = {
        "size": display_size.strip(),
        "resolution": resolution.strip(),
        "other_character": other_spec
    }
    return display_info


def parse_laptop_cpu_info(line):
    if line[:4] != "프로세서":
        print("cpu parse error")
        return
    line = line[5:]
    
    items = line.split(' /')
    keys = ["company", "generation", "code_name", "cpu_number", "core_num"]
    cpu_info = dict()
    for i, item in enumerate(items):
        if item:
            cpu_info[keys[i]] = item.strip()
    return cpu_info


def parse_laptop_memory_info(line):
    if line[:3] != "메모리":
        print("memory parse error")
        return
    line = line[4:]
    items = line.split(' /')

    memory_type = items[0]
    capacity = items[1].split(':')[1]
    other_character = items[2:]

    other_spec = [ i.strip() for i in other_character if i]
    memory_info = {
        "type": memory_type.strip(),
        "capacity": capacity.strip(),
        "other_character": other_spec,
    }
    return memory_info


def parse_laptop_storage_info(line):
    if line[:4] != "저장장치":
        print("storage parse error")
        return
    line = line[5:]
    items = line.split(' /')

    storage_type = items[0]
    capacity = items[1]
    storage_info = {
        "type": storage_type.strip(),
        "capacity": capacity.strip(),
    }
    return storage_info


def parse_laptop_graphic_card_info(line):
    if line[:3] != "그래픽":
        print("graphic card parse error")
        return
    line = line[4:]
    items = line.split(' /')

    graphic_type = items[0]
    graphic_name = items[1]

    graphic_card_info = {
        "type": graphic_type.strip(),
        "name": graphic_name.strip(),
    }
    return graphic_card_info


def parse_laptop_network_info(line):
    """
    ex>네트워크 무선랜: 802.11ax(Wi-Fi 6) / 유선랜: 기가비트 /
    """
    if line[:4] != "네트워크":
        print("network parse error")
        return
    line = line[5:]
    items = line.split(' /')

    network = {}
    for i in items:
        if i:
            cur = i.split(':')
            if cur[0] in ["무선랜", "유선랜"] and len(cur) == 2:
                t, spec = cur
                network[t.strip()] = spec.strip()
    return network


def parse_laptop_video_io_info(line):
    """
    ex> 영상입출력 HDMI 2.0 / 웹캠(HD) /
    """
    if line[:5] != "영상입출력":
        print("video io parse error")
        return
    line = line[6:]
    items = line.split(' /')

    video_io_info = [ i.strip() for i in items if i]
    return video_io_info


def parse_laptop_io_port_info(line):
    """
    ex> 단자 썬더볼트4: 1개(USB-C겸용) / USB-A: 3개 / USB 4.0 / USB 3.0 /
    """
    if line[:2] != "단자":
        print("io port parse error")
        return
    line = line[3:]
    items = line.split(' /')

    io_port_info = [ i.strip() for i in items if i]
    return io_port_info


def parse_laptop_other_character(line):
    """
    ex> 부가기능 얼굴 인식 / 웹캠OFF 지원 / 고속충전 / USB-PD / DP Alt Mode / MIL-STD /
    """
    if line[:4] != "부가기능":
        print("other_character parse error")
        return
    line = line[5:]
    items = line.split(' /')

    other_character = [ i.strip() for i in items if i]
    return other_character


def parse_laptop_input_device(line):
    """
    ex> 입력장치 키보드 라이트 / 침수지연키보드 / ㅡ형 방향키 / 숫자 키패드(4열) /
    """
    if line[:4] != "입력장치":
        print("input_device parse error")
        return
    line = line[5:]
    items = line.split(' /')

    input_device = [ i.strip() for i in items if i]
    return input_device


def parse_laptop_power_info(line):
    """
    ex>파워 배터리: 51.3Wh / 어댑터: 65W / 충전단자: DC /
    """
    if line[:2] != "파워":
        print("power_info parse error")
        return
    line = line[3:]
    items = line.split(' /')

    power_info = [ i.strip() for i in items if i]
    return power_info


def parse_laptop_specification(line):
    """
    ex>주요제원 두께: 19.9mm / 무게: 1.74kg / 색상: 실버
    """
    if line[:4] != "파워":
        print("specification parse error")
        return
    line = line[5:]
    items = line.split(' /')

    specification = [ i.strip() for i in items if i]
    return specification


def parse_laptop_price(price_list):
    """
    ex>'13몰', '2,999,000원 가격정보 더보기', 'SSD 512GB'
    """
    prices = []
    for i in range(0, len(price_list), 3):
        line = price_list[i+1]
        price = line[:-10]
        price.replace(',', '')

        option = price_list[i+2:]
        if option == []:
            option = ''
        else:
            option = option[0]

        prices.append({
            "price": price,
            "option": option,
            "market_num": price_list[i],
        })
        
    return prices


def parse_laptop_text(product_text):
    laptop = {}

    lines = product_text.split('\n')
    if lines[0] == '': return None

    manufacturer, name                    = parse_laptop_name(lines[0])
    is2in1, osinfo, spec_changed, purpose = parse_laptop_general_info(lines[1])
    if is2in1 == "중고": return None


    display_info = ''
    cpu_info = ''
    memory_info = ''
    storage_info = ''
    graphic_card_info = ''
    network_info = ''
    video_io_info = ''
    io_port_info = ''
    other_character = ''
    input_device = ''
    power_info = ''

    for i in range(2, 13):
        if   "화면정보" == lines[i][:4]: display_info = parse_laptop_display_info(lines[i])
        elif "프로세서" == lines[i][:4]: cpu_info     = parse_laptop_cpu_info(lines[i])
        elif "메모리"   == lines[i][:3]: memory_info  = parse_laptop_memory_info(lines[i])
        elif "저장장치" == lines[i][:4]: storage_info = parse_laptop_storage_info(lines[i])
        elif "그래픽"   == lines[i][:3]: graphic_card_info = parse_laptop_graphic_card_info(lines[i])
        elif "네트워크" == lines[i][:4]: network_info      = parse_laptop_network_info(lines[i])
        elif "영상입출력" == lines[i][:5]: video_io_info   = parse_laptop_video_io_info(lines[i])
        elif "단자"     == lines[i][:2]: io_port_info      = parse_laptop_io_port_info(lines[i])
        elif "부가기능" == lines[i][:4]: other_character   = parse_laptop_other_character(lines[i])
        elif "입력장치" == lines[i][:4]: input_device      = parse_laptop_input_device(lines[i])
        elif "파워"     == lines[i][:2]: power_info        = parse_laptop_power_info(lines[i])

    for i in range(len(lines)-1, 12, -1):
        if lines[i] in ["관심상품", "브랜드로그"]:
            break
    price             = parse_laptop_price(lines[i+1:])

    laptop = {
        "manufacturer": manufacturer,
        "name": name,
        "is2in1": is2in1,
        "osinfo": osinfo,
        "spec_changed": spec_changed,
        "purpose": purpose,
        
        "display": display_info,
        "cpu": cpu_info,
        "memory": memory_info,
        "storage": storage_info,
        "graphic_card": graphic_card_info,
        "network": network_info,
        "video_io": video_io_info,
        "io_port": io_port_info,
        "other_character": other_character,
        "input_device": input_device,
        "power": power_info,

        "price": price,
    }
    return laptop


def get_danawa_laptop_info_selenium(page=1):
    product_list = laptop_search.danawa_laptop_list(page)

    laptop_info = []
    for product in product_list:
        laptop = parse_laptop_text(product.text)
        if laptop:
            laptop_info.append(laptop)
    laptop_info = laptop_info[:-1]
    return laptop_info


if __name__=="__main__":
    parse_laptop_text("")
    laptop_search.quit_driver()
