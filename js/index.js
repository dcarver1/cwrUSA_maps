//create a filter manager to control the selection of items from a CSV file
var filter_manager;

$( function() {

    filter_manager = new Filter_Manager({
    csv:"./allMetricData2021-04-12_forfigsonly.csv",
     omit_result_item:["file_path","id"], // define which attributes not to show when a selection is made
     omit_filter_item:["Taxon","file_path","id"],
     path_col:"file_path",
     title_col:"Taxon",
     sub_title_col:"Associated crop",
     params:getParams(window.location.href),
     })
     // initialize this filtering system
     filter_manager.init();
    $("#search").focus();
    $("#search_clear").click(function(){
     $("#search").val("")

    })
    //auto adjusting frame height
    $('iframe').load(function() {
        //fade out the overlay;
      if($("iframe").attr("src")!=""){
       $(".overlay").fadeOut();
         //inject some css to iframe
        $("iframe").contents().find("head").append("<style>*{box-sizing:content-box;-webkit-box-sizing: content-box;}.col-md-3 {width: auto;}</style>");

      }
           });
    // adjust the size of the windows depending on the view
    /*
    ____________
    |  header  |
    ------------
    |c1|c2| c3 |

    */
    $( window ).resize(function() {
        var header_height=$("#header").height();
        var window_height= $(window).height()
        var window_width= $(window).width()

        $("#filter_area").height(window_height-header_height-40)

        $("#content").height(window_height-header_height-40)
    });
    $( window ).trigger("resize")

});
