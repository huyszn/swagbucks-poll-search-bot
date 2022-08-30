"""MIT License

Copyright (c) 2022 Huy Mai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import time, webbrowser, random

links = ['https://www.swagbucks.com/g/l/xcq6yq',
        'https://www.swagbucks.com/g/l/6vyye1',
        'https://www.swagbucks.com/g/l/p3btd7',
        'https://www.swagbucks.com/g/l/1j26i4']


def main():

    # daily poll
    print('poll')
    webbrowser.open('https://www.swagbucks.com/polls')
    time.sleep(10)

    print('Begin first search win')

    # first search win
    for url in links:
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

if __name__ == '__main__':
    main()