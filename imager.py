import crawler
import sys


def main(args):
    query = sys.argv[1]
    num_imgs = int(sys.argv[2])
    images_path = sys.argv[3]
    url = "https://google.com/search?q="+query

    c = crawler.Crawler(query, num_imgs, images_path)
    c.get_imgs()


if __name__ == '__main__':
    main(sys.argv)
