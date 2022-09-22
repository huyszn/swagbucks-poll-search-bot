import time, webbrowser, random

links = ['https://www.swagbucks.com/g/l/xcq6yq',
        'https://www.swagbucks.com/g/l/6vyye1',
        'https://www.swagbucks.com/g/l/p3btd7',
        'https://www.swagbucks.com/g/l/1j26i4']


def main():

    # daily poll
    print('Opening the poll section...')
    webbrowser.open('https://www.swagbucks.com/polls')
    time.sleep(10)

    print('Begin first search win')

    # first search win
    for url in (x for _ in range(1) for x in links):
        webbrowser.open(url)
        time.sleep(16)

    print('Begin second search win')

    # second search win
    #for _ in range(8):
    #    for x in links:
    #        print(x)
    for url in (x for _ in range(8) for x in links):
        webbrowser.open(url)
        time.sleep(16)
    
    webbrowser.open(random.choice(links))
    print('Finished running bot')

if __name__ == '__main__':
    main()