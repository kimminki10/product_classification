from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time


class LaptopSearch():
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument("disable-gpu")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(2)


    def get_driver(self):
        return self.driver


    def danawa_laptop_list(self, page):
        # 신상품순 정렬 페이지 이동
        self.driver.get("http://prod.danawa.com/list/?cate=112758&15main_11_02")
        self.driver.find_element(By.CSS_SELECTOR, "div.prod_list_opts > div.order_opt > ul > li[data-sort-method=NEW] > a").click()
        if page != 1:
            self.driver.execute_script(f"javascript:movePage({page})")
        time.sleep(2)
        product_list = self.driver.find_elements(By.CSS_SELECTOR, "#productListArea > div.main_prodlist.main_prodlist_list > ul > li")
        return product_list


    def parse_gpu_elem(self, element):
        gpu_info = {}

        pos = element.find_element(By.CLASS_NAME, "gg_pos").get_attribute('innerText')
        specs_list = element.find_elements(By.CLASS_NAME, "specs")
        value_list = element.find_elements(By.CLASS_NAME, "value")

        general_header = ["name", "codename", "shaders", "corespeed", "boost/Turbo", "memory_speed", "memory_bus", "memory_type"]
        performance_header = ["performance_rating", "3DMarkIceStormGPU", "3DMarkCloudGateGPU", "3DMark11PGPU", "3DMarkFireStrikeGraphics", "3DMarkTimeSpyGraphics"]

        gpu_info["pos"] = pos.strip()
        for spec, key in zip(specs_list[1:], general_header):
            gpu_info[key] = spec.get_attribute('innerText')
        
        for value, key in zip(value_list, performance_header):
            t = ''
            if value.text != '':
                t = value.find_element(By.CSS_SELECTOR, "span.bl_ch_value > span").text
            gpu_info[key] = t

        return gpu_info


    def notebook_benchmark(self):
        self.driver.get("https://www.notebookcheck.net/Mobile-Graphics-Cards-Benchmark-List.844.0.html?type=&sort=&showClassDescription=1&archive=1&perfrating=1&or=0&showBars=1&3dmark13_ice_gpu=1&3dmark13_cloud_gpu=1&3dmark11_gpu=1&3dmark13_fire_gpu=1&3dmark13_time_spy_gpu=1&gpu_fullname=1&architecture=1&pixelshaders=1&vertexshaders=1&corespeed=1&boostspeed=1&memoryspeed=1&memorybus=1&memorytype=1")
        time.sleep(2)

        gpu_list = self.driver.find_elements(By.CSS_SELECTOR, "tbody > tr.odd,tr.even")
        laptop_gpu_list = [self.parse_gpu_elem(elem) for elem in gpu_list]
        return laptop_gpu_list


    def parse_game_elem(self, element, game_code):
        benchmark = {}
        pos = element.find_element(By.CSS_SELECTOR, "span.gg_pos").get_attribute('innerText')
        name = element.find_element(By.CSS_SELECTOR, "td.specs.fullname").get_attribute('innerText')

        benchmark['GPU'] = {
            "pos": pos,
            "name": name,
            "game_code": game_code
        }

        game_bench_elems = element.find_elements(By.CSS_SELECTOR, f"td.gg_fld")
        game_bench = []
        for elem in game_bench_elems:
            t = elem.get_attribute('innerText')
            class_name = elem.get_attribute('class').split(' ')[0]
            game_bench.append({
                "value": t,
                "type": class_name
            })
            
        benchmark['game_bench'] = game_bench
        return benchmark
        

    def game_benchmark(self, game_code):
        url = f"https://www.notebookcheck.net/Computer-Games-on-Laptop-Graphics-Cards.13849.0.html?type=&sort=&professional=2&multiplegpus=1&archive=1&or=0&gpu_fullname=1&gameselect%5B%5D={game_code}"
        self.driver.get(url)
        time.sleep(2)

        benchmark_list = self.driver.find_elements(By.CSS_SELECTOR, "tbody > tr.odd,tr.even")
        laptop_bench_list = [self.parse_game_elem(e, game_code) for e in benchmark_list]
        return laptop_bench_list

    def quit_driver(self):
        self.driver.quit()


laptop_search = LaptopSearch()

if __name__=="__main__":
    game_benchmark_list = laptop_search.game_benchmark(686)
    for row in game_benchmark_list:
        print(row)
    laptop_search.quit_driver()