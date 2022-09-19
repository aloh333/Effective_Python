from unittest import TestCase, main


def setUpModule():
    print('* 모듈 설정')


def tearDownModule():
    print('* 모듈 정리')


class IntegrationTest(TestCase):
    def setUp(self) -> None:
        print('* 테스트 설정')

    def tearDown(self) -> None:
        print('* 테스트 정리')

    def test_end_to_end1(self):
        print('* 테스트 1')

    def test_end_to_end2(self):
        print('* 테스트 2')


if __name__ == '__main__':
    main()