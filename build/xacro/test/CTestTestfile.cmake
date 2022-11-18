# CMake generated Testfile for 
# Source directory: /home/student/humble_ws/een150-2022-a4-group-group18/xacro_2.0.7./test
# Build directory: /home/student/humble_ws/build/xacro/test
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(pytest "/usr/bin/python3.10" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/home/student/humble_ws/build/xacro/test_results/xacro/pytest.xunit.xml" "--package-name" "xacro" "--output-file" "/home/student/humble_ws/build/xacro/ament_cmake_pytest/pytest.txt" "--env" "AMENT_PREFIX_PATH=/home/student/humble_ws/build/xacro/test/test_ament_index:/home/student/requirements_ws/install/visualization_server:/home/student/requirements_ws/install/ur_script_driver:/home/student/requirements_ws/install/ur_controller:/home/student/requirements_ws/install/simple_robot_simulator:/home/student/requirements_ws/install/ur_script_msgs:/home/student/requirements_ws/install/ur_description:/home/student/requirements_ws/install/ur_controller_msgs:/home/student/requirements_ws/install/simple_robot_simulator_msgs:/home/student/requirements_ws/install/simple_robot_simulator_bringup:/home/student/requirements_ws/install/scene_manipulation_service:/home/student/requirements_ws/install/scene_manipulation_bringup:/home/student/requirements_ws/install/scene_manipulation_msgs:/home/student/requirements_ws/install/scene_manipulation_marker:/home/student/requirements_ws/install/scene_manipulation_gui:/home/student/requirements_ws/install/panda_description:/home/student/requirements_ws/install/meca_description:/home/student/requirements_ws/install/gui_tools:/opt/ros/humble" "--command" "/usr/bin/python3.10" "-u" "-m" "pytest" "/home/student/humble_ws/een150-2022-a4-group-group18/xacro_2.0.7./test/." "-o" "cache_dir=/home/student/humble_ws/build/xacro/test/ament_cmake_pytest/pytest/.cache" "--junit-xml=/home/student/humble_ws/build/xacro/test_results/xacro/pytest.xunit.xml" "--junit-prefix=xacro")
set_tests_properties(pytest PROPERTIES  LABELS "pytest" TIMEOUT "60" WORKING_DIRECTORY "/home/student/humble_ws/een150-2022-a4-group-group18/xacro_2.0.7./test" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_pytest/cmake/ament_add_pytest_test.cmake;169;ament_add_test;/home/student/humble_ws/een150-2022-a4-group-group18/xacro_2.0.7./test/CMakeLists.txt;10;ament_add_pytest_test;/home/student/humble_ws/een150-2022-a4-group-group18/xacro_2.0.7./test/CMakeLists.txt;0;")
add_test(xacro_cmake "/home/student/humble_ws/een150-2022-a4-group-group18/xacro_2.0.7./test/test-cmake.sh" "/home/student/humble_ws/een150-2022-a4-group-group18/xacro_2.0.7./test/test-xacro-cmake")
set_tests_properties(xacro_cmake PROPERTIES  _BACKTRACE_TRIPLES "/home/student/humble_ws/een150-2022-a4-group-group18/xacro_2.0.7./test/CMakeLists.txt;15;add_test;/home/student/humble_ws/een150-2022-a4-group-group18/xacro_2.0.7./test/CMakeLists.txt;0;")
