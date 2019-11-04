from selenium import webdriver
from bs4 import BeautifulSoup
import os
import re
import random
import time


driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)

def get_user_list(limit):
    page = 1
    user_list = []
    while len(user_list) <= limit:
        driver.get('https://movie.naver.com/movie/point/af/list.nhn?&page={0}'.format(page))

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        reviewNum = soup.select('#old_content > table > tbody > tr > td.ac.num')
        userId = soup.select('table.list_netizen > tbody > tr > td > a.author')

        for i in range(len(reviewNum)):
            review = str(reviewNum[i]).replace('<td class="ac num">','').replace('</td>','')
            user = userId[i].text.replace('*','')
            if user not in [user[1] for user in user_list]:
                user_list.append((review, user))

        time.sleep(random.randrange(2, 5))
        page += 1

    return user_list[:limit]

def get_movie_link(soup):
    movie_links = soup.select('a[href]')

    movie_links_list = []
    for link in movie_links:
        if re.search(r'st=mcode&sword' and r'&target=after$', link['href']):
            target_url = 'https://movie.naver.com/movie/point/af/list.nhn'+str(link['href'])
            movie_links_list.append(target_url)
    
    return movie_links_list[1:]

def get_review(reviewNo):
    user_reviews = []

    '''
    dirver & beautifulsoup init
    '''

    # 영화 링크를 가져오는 코드
    movie_links = get_movie_link(soup)
    movieId = [link.replace('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=','').replace('&target=after','') for link in movie_links]
    
    '''
    crawling information
    '''
    
    time.sleep(random.randrange(3, 5))

    return user_reviews

def main():
    print(get_user_list(5))
    driver.close()


if __name__ == "__main__":
    main()
