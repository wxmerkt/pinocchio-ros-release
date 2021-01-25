//
// Copyright (c) 2016-2020 CNRS INRIA
//

#ifndef __pinocchio_utils_file_explorer_hpp__
#define __pinocchio_utils_file_explorer_hpp__

#include <string>
#include <vector>

#include "pinocchio/config.hpp"

namespace pinocchio
{

  /**
   * @brief      Parse an environment variable if exists and extract paths according to the delimiter.
   *
   * @param[in]  env_var_name The name of the environment variable.
   * @param[in]  delimiter The delimiter between two consecutive paths.
   *
   * @return The vector of paths extracted from the environment variable value.
   */
  PINOCCHIO_DLLAPI std::vector<std::string>
  extractPathFromEnvVar(const std::string & env_var_name,
                        const std::string & delimiter = ":");


  /**
   * @brief      Parse an environment variable if exists and extract paths according to the delimiter.
   *
   * @param[in]  env_var_name The name of the environment variable.
   * @param[out] list_of_paths List of path to fill with the paths extracted from the environment variable value.
   * @param[in]  delimiter The delimiter between two consecutive paths.
   */
  PINOCCHIO_DLLAPI void
  extractPathFromEnvVar(const std::string & env_var_name,
                        std::vector<std::string> & list_of_paths,
                        const std::string & delimiter = ":");


  /**
   * @brief      Parse the environment variable ROS_PACKAGE_PATH and extract paths
   *
   * @return     The vector of paths extracted from the environment variable ROS_PACKAGE_PATH
   */
  PINOCCHIO_DLLAPI std::vector<std::string> rosPaths();

}

#endif // __pinocchio_utils_file_explorer_hpp__
