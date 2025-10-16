# Logging Information Document

This doc describes the process for adding logging for a project.
Share with the user on which step you are after you preform each step

The steps for adding logging to a C++ project:
1. Stage 1: Identify logging utilities (or create one for the project)
   1. Read the project and search for logging utilities
   2. If logging utilities exists, use them to add logging in the same format (jump to "Stage 2"). If not, continue with the next instructions to create logging utility for the project
   3. If not exists, create a "logger.hpp" file under "include" folder, which contains:
        """
         #include <iostream>
         #include <string>
         #include <chrono>
         #include <ctime>
         #include <iomanip> // For std::put_time

         class Logger {
         public:
            enum LogLevel {
               INFO,
               WARNING,
               ERROR
            };

            // Static method to log messages
            static void log(LogLevel level, const std::string& message) {
               std::cout << formatMessage(level, message) << std::endl;
            }

         private:
            // Private static helper to format log messages
            static std::string formatMessage(LogLevel level, const std::string& message) {
               std::string levelString;
               switch (level) {
                     case INFO:
                        levelString = "INFO";
                        break;
                     case WARNING:
                        levelString = "WARNING";
                        break;
                     case ERROR:
                        levelString = "ERROR";
                        break;
               }

               // Get current time
               auto now = std::chrono::system_clock::now();
               std::time_t currentTime = std::chrono::system_clock::to_time_t(now);
               std::stringstream ss;
               ss << std::put_time(std::localtime(&currentTime), "%Y-%m-%d %H:%M:%S");

               return "[" + ss.str() + "] [" + levelString + "] " + message;
            }

            // Private constructor to prevent instantiation (optional, if you want a purely static logger)
            Logger() = delete;
            Logger(const Logger&) = delete;
            Logger& operator=(const Logger&) = delete;
         };

        """
2. Stage 2: Identify where to add calls to logger: 
   1. Intentify places for logger - code path with critical functionality
   2. Use "Info" logging level as default, but you can also use "Error" or "Critical" according to the context of the running code
   3. Create a temporary "LoggingSuggestions.md" file, and write there where you plan to add loggers, and on which level, to inform the user. Ask for approval
3. Stage 3: Add logs
   1. Include the "logger.hpp" file or the other logging utility header
   2. Add the code blocks calling the logger, where you specified in "LoggingSuggestions.md", and delete the file
4. Stage 4: Provide a short summary
   1. Inform the user to where loggers were added