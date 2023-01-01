
class A:
    _underscore_class_var = 100

    @staticmethod
    def _under_score_method():
        print('_under_score_method')

    __double_underscore_class_var = 100

    @staticmethod
    def __double_under_score_method():
        print('_double_under_score_method')
