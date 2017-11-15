import sys
import yuzhouhuang_scheduler
import course_dictionary


def main(argv):
    # Tests if course_dictionary is valid

    test = course_dictionary.create_course_dict()
    # # Test to see if all prereqs are in the file.
    # prereq_list = [single_course for vals in test.values()
    #                for some_prereqs in vals.prereqs for single_course in some_prereqs]
    # for prereq in prereq_list:
    #     if prereq not in test:
    #         print(prereq)
    # for key in test:
    #     # Test to see if every course has a term and credits.
    #     if not test[key].terms or not test[key].credits:
    #         print(key)
    #     # Test to see if a course's prereqs include the course itself
    #     # if key in [course for prereq in test[key].prereqs for course in prereq]:
    #     #     print(key)
    # Prints all the CS courses.
    # for key in test:
    #     if key.program == 'CS':
    #         print(key, test[key])
    # Prints the entire dictionary.
    # yuzhouhuang_scheduler.print_dict(test)
    # print(test[('CS', 'open3')])
    # print('Done')

    # for p in yuzhouhuang_scheduler.create_course_operators(test):
    #     print(p)

    basic_plan = yuzhouhuang_scheduler.course_scheduler(test, [yuzhouhuang_scheduler.Course('CS', '2231'),
                                                               yuzhouhuang_scheduler.Course('CS', '3251'),
                                                               yuzhouhuang_scheduler.Course('CS', 'statsprobability')],
                                                        [yuzhouhuang_scheduler.Course('MATH', '2810'),
                                                         yuzhouhuang_scheduler.Course('MATH', '2820'),
                                                         yuzhouhuang_scheduler.Course('MATH', '3640')])
    yuzhouhuang_scheduler.print_dict(basic_plan)


if __name__ == "__main__":
    main(sys.argv)
