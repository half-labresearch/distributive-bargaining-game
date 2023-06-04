$(function (){
    var $divFormAmountOffered = $("[name=amount_offered]").closest("._formfield");
    var $divMakeNewOffer =  $("[name=make_new_offer]").closest("._formfield")
    $divFormAmountOffered.hide();
    $divMakeNewOffer.hide();
    var offerAcceptedFieldExists = $("[name=offer_accepted]").length > 0;
    var makeNewOfferExists = $("[name=make_new_offer]").length > 0;

    if(offerAcceptedFieldExists){
        $("[name=offer_accepted][value=True]").prop('checked', true);

        /****** events ******/
        $("[name=offer_accepted]").on('change', function () {
            let hasAccepted= $(this).val() == "True";
            if(!hasAccepted){
                $("[name=make_new_offer][value=False]").prop('checked', true);
                $divMakeNewOffer.show();
            }else{
                $divMakeNewOffer.hide();
                $divFormAmountOffered.hide();
            }
        })
    }

    $("[name=make_new_offer]").on('change', function (){
        let makeNewOffer = $(this).val() == "True";
        if(makeNewOffer){
            $divFormAmountOffered.show();
        }else{
            $divFormAmountOffered.hide();
        }
    })

    $('#form').submit(function () {
        //reset offer to the initial value
        if(offerAcceptedFieldExists && makeNewOfferExists){
            if($("[name=offer_accepted]").val() == "True" || $("[name=make_new_offer]") == "False"){
                $("[name=amount_offered]").val(originalOffer);
            }
        }

    })
})


function parseBooleanToJS(str){
    return str == null ? str : JSON.parse('False'.toLowerCase());
}