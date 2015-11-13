// Instrument Filters
expSettingsApp.filter('isAWG', function() {
    return function(input) {
        var out = []
        angular.forEach(input, function(each) {
            if (each.x__module__ == 'instruments.AWGs') {
                out.push(each)
            }
        });
        return out;
    }
});

expSettingsApp.filter('isMicrowaveSource', function() {
    return function(input) {
        var out = []
        angular.forEach(input, function(each) {
            if (each.x__module__ == 'instruments.MicrowaveSources') {
                out.push(each)
            }
        });
        return out;
    }
});

expSettingsApp.filter('isOther', function() {
    return function(input) {
        var out = []
        angular.forEach(input, function(each) {
            if (each.x__module__ != 'instruments.MicrowaveSources' && each.x__module__ != 'instruments.AWGs') {
                out.push(each)
            }
        });
        return out;
    }
});

// Channel Filters
expSettingsApp.filter('isPhysical', function() {
    return function(input) {
        var out = []
        angular.forEach(input, function(each) {
            if (each.x__class__.indexOf('Physical') > -1) {
                out.push(each)
            }
        });
        return out;
    }
});

expSettingsApp.filter('isLogical', function() {
    return function(input) {
        var out = []
        angular.forEach(input, function(each) {
            if (each.x__class__.indexOf('Logical') > -1 || each.x__class__.indexOf('Physical') == -1) {
                out.push(each)
            }
        });
        return out;
    }
});
