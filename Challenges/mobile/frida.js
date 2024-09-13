Java.perform(function() {

    var str = Java.use('java.lang.String');

    str.equals.overload('java.lang.Object').implementation = function(obj) {
        var response = str.equals.overload('java.lang.Object').call(this, obj);
        if (obj) {
            if (obj.toString() == "admin" || obj.toString() == "a2a3d412e92d896134d9c9126d756f") {

                send("Is " + str.toString.call(this) + " == " + obj.toString() + "? " + response);
                return true;
            }
        }
        return response;
    }

});
