expSettingsApp.controller('mainCtrl', [
    '$scope', '$http', '$state', function($scope, $http, $state) {
    $scope.model = {
        message: 'This is the controller for dealing with the experiment settings'
    };

    $state.go("root");

	this.getSettings = function () {
		$http.get('/settings').success(function (data, status, headers, config){
			$scope.settings = data;
		});
	};

	this.getLibraries = function() {
		$http.get('/libraries').success(function (data, status, headers, config) {
			$scope.instrs = [];
			angular.forEach(data.instrs.instrDict, function (value, key) {
				this.push(value);
			}, $scope.instrs);

			$scope.channels = [];
			angular.forEach(data.channels.channelDict, function (value, key) {
				this.push(value);
			}, $scope.channels);

			$scope.measurements = [];
			angular.forEach(data.measurements.filterDict, function (value, key) {
				this.push(value);
			}, $scope.measurements);

			$scope.sweeps = [];
			angular.forEach(data.sweeps.sweepDict, function (value, key) {
				this.push(value);
			}, $scope.sweeps);
		}).then(function() {
			$scope.selectedChan = $scope.channels[0];
			$scope.selectedInstr = $scope.instrs[0];
			$scope.selectedMeas = $scope.measurements[0];
			$scope.selectedSweep = $scope.sweeps[0];
		});
	};

	this.getSettings();
	this.getLibraries();

	// this.getPhysicalChannels = function () {
	// 	$scope.physicalChannels = []
	// 	for (var index in $scope.channels) {
	// 		if($scope.channels[index].x__class__.indexOf("Physical") > -1) {
	// 			channels.push($scope.channels[index]);
	// 		};
	// 	}
	// 	return $scope.physicalChannels;
	// }

	// this.logicalChannels = function () {
	// 	var channels = []
	// 	for (var index in $scope.channels) {
	// 		if($scope.channels[index].x__class__.indexOf("Physical") == -1) {
	// 			channels.push($scope.channels[index]);
	// 		};
	// 	}
	// 	return channels;
	// }

	$scope.selectChan = function (channel) {
		$scope.selectedChan = channel;
	}

	this.sweeps = function() {
		return $scope.sweeps;
	};

	this.measurements = function () {
		return $scope.measurements;
	}

	this.microwaveSources = function () {
		var sources = []
		for (var index in $scope.instrs) {
			if ($scope.instrs[index].x__module__ == "instruments.MicrowaveSources") {
				sources.push($scope.instrs[index])
			};
		}
		return sources
	};

	this.AWGs = function () {
		var sources = []
		for (var index in $scope.instrs) {
			if ($scope.instrs[index].x__module__ == "instruments.AWGs") {
				sources.push($scope.instrs[index])
			};
		}
		return sources;
	}

	this.others = function () {
		var sources = []
		for (var index in $scope.instrs) {
			if (($scope.instrs[index].x__module__ != "instruments.MicrowaveSources") &&
				($scope.instrs[index].x__module__ != "instruments.AWGs")) {
				sources.push($scope.instrs[index])
			};
		}
		return sources
	}

	$scope.isAWG = function (instr) {
		return instr.x__module__ == "instruments.AWGs"
	}

}]);