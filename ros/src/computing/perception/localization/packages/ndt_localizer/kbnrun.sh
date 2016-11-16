CXX_FLAGS=" -DUSE_FAST_PCL -DNDEBUG -I/home/shihclin/Autoware/ros/devel/include -I/usr/include/vtk-5.8 -I/home/shihclin/Autoware/ros/src/computing/perception/localization/packages/ndt_localizer/include -I/home/shihclin/Autoware/ros/src/sensing/drivers/lidar/packages/velodyne/velodyne_pointcloud/include -I/home/shihclin/Autoware/ros/src/sensing/drivers/lidar/packages/velodyne/velodyne_driver/include -I/opt/ros/indigo/include -I/usr/include/eigen3 -I/usr/include/pcl-1.7 -I/usr/include/ni -I/home/shihclin/Autoware/ros/src/computing/perception/localization/packages/ndt_localizer/../../lib/fast_pcl/registration/include -I/home/shihclin/Autoware/ros/src/computing/perception/localization/packages/ndt_localizer/../../lib/fast_pcl/filters/include"
#CXX_FLAGS="-g -Wall -DUSE_FAST_PCL   -Wno-deprecated -fopenmp -O3 -DNDEBUG -I/home/shihclin/Autoware/ros/devel/include -I/usr/include/vtk-5.8 -I/home/shihclin/Autoware/ros/src/computing/perception/localization/packages/ndt_localizer/include -I/home/shihclin/Autoware/ros/src/sensing/drivers/lidar/packages/velodyne/velodyne_pointcloud/include -I/home/shihclin/Autoware/ros/src/sensing/drivers/lidar/packages/velodyne/velodyne_driver/include -I/opt/ros/indigo/include -I/usr/include/eigen3 -I/usr/include/pcl-1.7 -I/usr/include/ni -I/home/shihclin/Autoware/ros/src/computing/perception/localization/packages/ndt_localizer/../../lib/fast_pcl/registration/include -I/home/shihclin/Autoware/ros/src/computing/perception/localization/packages/ndt_localizer/../../lib/fast_pcl/filters/include"

CXX_DEFINES="-DDISABLE_PCAP -DDISABLE_PNG -DROSCONSOLE_BACKEND_LOG4CXX -DROS_BUILD_SHARED_LIBS=1 -DROS_PACKAGE_NAME=\"ndt_localizer\""

#/usr/bin/c++ -std=c++11 -O3 -c -o ndt_matching.cpp.o\

#/usr/bin/c++ -std=c++11 -Wall -O3 -c -o gpu_ndt_matching.o\
# pgc++ -std=c++11 -acc -ta=nvidia -Minfo=accel -O3 -c -o gpu_ndt_matching.o\



#pgc++ -w -std=c++11 -acc -ta=nvidia -Minfo=accel -O3 -c -o ndt_matching.o\
#/usr/bin/c++ -std=c++11 -c -o gpu_ndt_matching.orig.o\
#pgc++ -v -w -mp -std=c++11 -acc -ta=nvidia -Minfo=accel -c -o gpu_ndt_matching.o\
#pgc++ -v -w -mp -std=c++11 -acc -Minfo=accel -c -o gpu_ndt_matching.none.o\
# $CXX_FLAGS $CXX_DEFINES\
# -I../../lib/fast_pcl/registration/include/\
# -I../../lib/fast_pcl/filters/include\
# -I../../../../../sensing/drivers/lidar/packages/velodyne/velodyne_pointcloud/include\
# -I/usr/include/pcl-1.7/\
# nodes/gpu_ndt_matching/gpu_ndt_matching.cpp

 #nodes/ndt_matching/ndt_matching.cpp


#/usr/bin/c++   -std=c++11 -O2 -g -Wall -DUSE_FAST_PCL   -Wno-deprecated -fopenmp -O3 -DNDEBUG\
#pgc++  -w -mp -acc -ta=nvidia -Minfo=accel -std=c++11 -DUSE_FAST_PCL  -DNDEBUG\
pgc++  -w -mp -acc -Minfo=accel -std=c++11 -DUSE_FAST_PCL  -DNDEBUG\
  gpu_ndt_matching.none.o\
  -o gpu_ndt_matching\
 -rdynamic\
 /home/shihclin/Autoware/ros/devel/lib/libvelodyne_rawdata.so /opt/ros/indigo/lib/libpcl_ros_filters.so /opt/ros/indigo/lib/libpcl_ros_io.so /opt/ros/indigo/lib/libpcl_ros_tf.so -lpcl_common -lpcl_octree -lpcl_io -lpcl_kdtree -lpcl_search -lpcl_sample_consensus -lpcl_filters -lpcl_features -lpcl_keypoints -lpcl_segmentation -lpcl_visualization -lpcl_outofcore -lpcl_registration -lpcl_recognition -lpcl_surface -lpcl_people -lpcl_tracking -lpcl_apps -lboost_iostreams -lboost_serialization -lqhull -lOpenNI -Wl,-Bstatic -lflann_cpp_s -Wl,-Bdynamic /usr/lib/libvtkCommon.so.5.8.0 /usr/lib/libvtkRendering.so.5.8.0 /usr/lib/libvtkHybrid.so.5.8.0 /usr/lib/libvtkCharts.so.5.8.0 /opt/ros/indigo/lib/libdynamic_reconfigure_config_init_mutex.so /opt/ros/indigo/lib/librosbag.so /opt/ros/indigo/lib/librosbag_storage.so -lboost_program_options /opt/ros/indigo/lib/libroslz4.so -llz4 /opt/ros/indigo/lib/libtopic_tools.so /home/shihclin/Autoware/ros/devel/lib/libvelodyne_input.so /opt/ros/indigo/lib/libnodeletlib.so /opt/ros/indigo/lib/libbondcpp.so -luuid -ltinyxml /opt/ros/indigo/lib/libclass_loader.so -lPocoFoundation -ldl /opt/ros/indigo/lib/libroslib.so /opt/ros/indigo/lib/libtf.so /opt/ros/indigo/lib/libtf2_ros.so /opt/ros/indigo/lib/libactionlib.so /opt/ros/indigo/lib/libmessage_filters.so /opt/ros/indigo/lib/libroscpp.so -lboost_signals -lboost_filesystem /opt/ros/indigo/lib/libxmlrpcpp.so /opt/ros/indigo/lib/libtf2.so /opt/ros/indigo/lib/librosconsole.so /opt/ros/indigo/lib/librosconsole_log4cxx.so /opt/ros/indigo/lib/librosconsole_backend_interface.so -llog4cxx -lboost_regex /opt/ros/indigo/lib/libroscpp_serialization.so /opt/ros/indigo/lib/librostime.so -lboost_date_time /opt/ros/indigo/lib/libcpp_common.so -lboost_system -lboost_thread -lpthread -lconsole_bridge /home/shihclin/Autoware/ros/devel/lib/libfast_pcl_filters.so /home/shihclin/Autoware/ros/devel/lib/libfast_pcl_registration.so -lpcap -lyaml-cpp -Wl,-rpath,/home/shihclin/Autoware/ros/devel/lib:/opt/ros/indigo/lib
# -Wl,-rpath,/usr/lib/gcc/x86_64-linux-gnu/4.8.4\
# -rdynamic /usr/lib/gcc/x86_64-linux-gnu/4.8.4/libgomp.so -lgomp -lrt

