var myApp = angular.module('CreateTaskApp', []);

myApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

myApp.controller("CreateTaskController", function($scope, $http) {

    $scope.getUsername = function() {

    var get_current_url = '/tasks/api/current_user/';
    $http.get(get_current_url).success(

    function(response) {
        $scope.username = response.user;
        // console.log(task.username);
    },

    function errorCallback(response) {
        console.log(response);
    });

  }();



    $scope.createTask = function(task) {
        var config = {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
            }
        }


        var post_url ='/tasks/api/';
        $http.put(post_url,
            "done=" + encodeURIComponent('N') +
            "&title=" + encodeURIComponent(task.title) +
            "&description=" + encodeURIComponent(task.description) +
            "&created_by=" + encodeURIComponent($scope.username) +
            "&amended_by=" + encodeURIComponent($scope.username),
            config
        ).success(function(response) {
            $scope.SuccessMessage = "Task created";
            $scope.task.title = "";
            $scope.task.description = "";
        }, function errorCallback(response)
        {
          console.log(response);
        });
    }

});

var myTaskApp = angular.module('TaskApp', []);

myTaskApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);


myTaskApp.controller("MyController", function($scope, $http, $filter) {

    var get_url = '/tasks/api/current_user/';
    $http.get(get_url).success(function(response) {
        $scope.username = response.user;
    });



    $http.get('/tasks/api/?format=json').success(function(response) {

        $scope.tasks = response;
        // console.log($scope);
        // Update model
        angular.forEach($scope.tasks, function(task) {
            task.checked = task.done == 'Y' ? 1 : 0;
            if (task.checked) {
                task.myClass = "strikethrough";
            }


        });

        $scope.editTask = function(task){
          alert("TODO# Need to implement");
        }

        $scope.completedTask = function(){
            $scope.tasks = $filter('filter')($scope.tasks, {done: "N"});

        }

        // $scope.allTasks = function(){
        //     $scope.tasks = $filter('filter')($scope.tasks, {});
        // }

        $scope.deleteTask = function(task) {
            if (confirm('Are you sure you want to delete this?')) {
                var delete_url = '/tasks/api/delete/' + task.id + '/';
                var config = {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
                    }
                }
                $http.delete(delete_url,
                    '',
                    config
                ).success(function(response) {
                    $scope.refresh();
                }, function errorCallback(response) {
                    console.log(response);
                });

                $scope.refresh = function() {
                    $http.get('/tasks/api/?format=json')
                        .success(function(data) {
                            $scope.tasks = data;

                            angular.forEach($scope.tasks, function(task) {
                                task.checked = task.done == 'Y' ? 1 : 0;
                                if (task.checked) {
                                    task.myClass = "strikethrough";
                                }

                            });

                        });
                }

            }


        }



        $scope.updateTask = function(task) {

           elm = document.querySelector('#tasklist' + task.id)
            if (elm.classList.contains('strikethrough')) {
                angular.element(elm).removeClass('strikethrough');
            } else {
                angular.element(elm).addClass('strikethrough');
            }
            task.done = task.checked ? 'N' : 'Y';
            var config = {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
                }
            }
            var post_url = '/tasks/api/' + task.id + '/';
            $http.put(post_url,
                "done=" + encodeURIComponent(task.done) +
                "&title=" + encodeURIComponent(task.title) +
                "&description=" + encodeURIComponent(task.description) +
                "&amended_by=" + encodeURIComponent($scope.username),

                config
            ).success(function(response) {
                console.log(response);
            }, function errorCallback(response) {
                console.log(response);
            });
            task.myClass = task.checked ? "strikethrough" : "";
        };

    });
});
