$(function(){

// 최초실행 --------------------------------    
    let no = [1,2,3,4,5,6,7,8,9,10];
    let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','최현묵','이규원'];
    let kor = [62,90,64,76,51,89,77,55,73,53];
    let eng = [70,62,73,54,55,60,67,77,51,100];
    let math = [81,79,50,83,72,79,82,86,50,94];
    let total = [213,231,187,213,178,228,226,218,174,247];
    let avg = [71,77,62.3,71,59.3,76,75.3,72.7,58,82.3];

    // tbody부분 10개 행 생성
    let htmlData = "";
    for (let i=0;i<no.length;i++){
        htmlData += "<tr id='"+no[i]+"'>";
        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+no[i]+"'></td>";
        htmlData += "<td>"+no[i]+"</td>";
        htmlData += "<td>"+name[i]+"</td>";
        htmlData += "<td>"+kor[i]+"</td>";
        htmlData += "<td>"+eng[i]+"</td>";
        htmlData += "<td>"+math[i]+"</td>";
        htmlData += "<td>"+total[i]+"</td>";
        htmlData += "<td>"+avg[i]+"</td>";
        htmlData += "<td>0</td>";
        htmlData += "<td><button class='delBtn'>삭제</button></td>";
        htmlData += "</tr>";
    }//for

    // html소스를 tbody 추가
    $("#body").html(htmlData);

// 최초실행 -------------------------------- 

    //학생입력버튼 클릭
    $("#writeBtn").click(function(){
        $(".p_all").css("display","block");
    });

    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");
    })




    //학생입력확인 버튼
    $("#confirmBtn").on("click",function(){
        // 글자-text() innerText, input-val() value, html() innerHtml
        //console.log(Math.max.apply(null,no)+1); //배열에서 최대값 구하기
        //no.push(Math.max.apply(null,no)+1); //배열추가
        console.log("이름 : "+$("#name").val());
        
        //공백확인
        if($("#name").val().length<2){
            alert("이름을 입력하셔야 등록이 가능합니다.");
            $("#name").focus();
            return false;
        }
        
        //번호생성은 DB에서 자동으로 부여
        let i_no = Math.max.apply(null,no)+1;
        no.push(i_no);
        let i_name = $("#name").val(); //String
        let i_kor = Number($("#kor").val());
        let i_eng = Number($("#eng").val());
        let i_math = Number($("#math").val());
        let i_total = i_kor+i_eng+i_math;
        let i_avg = (i_total/3).toFixed(2); //소수점2자리 반올림

        //table tr추가
        let htmlData = "";
        htmlData += "<tr id='"+i_no+"'>";
        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+i_no+"'></td>";
        htmlData += "<td>"+i_no+"</td>";
        htmlData += "<td>"+i_name+"</td>";
        htmlData += "<td>"+i_kor+"</td>";
        htmlData += "<td>"+i_eng+"</td>";
        htmlData += "<td>"+i_math+"</td>";
        htmlData += "<td>"+i_total+"</td>";
        htmlData += "<td>"+i_avg+"</td>";
        htmlData += "<td>0</td>";
        htmlData += "<td><button class='delBtn'>삭제</button></td>";
        htmlData += "</tr>";

        // html소스를 tbody 추가
        //$("#body").html(htmlData); //기존html에 덮어쓰기
        //$("#body").prepend(htmlData); //기존html 위쪽에 추가
        $("#body").append(htmlData); //기존html 뒤쪽에 추가
        
        //input 초기화
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
        $(".p_all").css("display","none");
        
    });//학생입력버튼


    //전체선택,취소
    $("#allChk").click(function(){
        if($(this).is(":checked")==true){
            $(".stuChk").each(function(){
                $(this).prop("checked",true);
            })
        }else{
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            })
        }
    });


    //table에 있는 삭제버튼 클릭
    $(document).on("click",".delBtn",function(){
        console.log("현재 선택된 class id : "+$(this).parent().parent().attr("id"));
        if(confirm("정말 삭제하시겠습니까?")){
            $("#"+$(this).parent().parent().attr("id")).remove();
        }
    });//table삭제

    // 동적으로 할당될 경우 실행이 안됨.
    // $(".delBtn").on("click",function(){
    //     console.log("현재 선택된 class id : "+$(this).parent().parent().attr("id"));
    //     if(confirm("정말 삭제하시겠습니까?")){
    //         $("#"+$(this).parent().parent().attr("id")).remove();
    //     }
    // });//table삭제

    //하단 삭제버튼 클릭
    $("#deleteBtn").click(function(){
        //alert("test");
        console.log("체크박스 개수 : "+$(".stuChk").length);
        console.log("체크박스에서 체크된 개수 : "+$(".stuChk:checked").length);
        console.log("체크박스에서 체크된 개수 : "+$("input:checkbox[name='stu']:checked").length);
        
        //체크되어 있는 것이 없을 경우
        if($(".stuChk:checked").length<1){
            alert("삭제할 데이터를 체크해주셔야 가능합니다.");
            return false;
        }//체크if

        //현재 체크박스가 체크가 되어 있는지 확인
        if(!confirm("정말 삭제하시겠습니까?")){
            return false; //no버튼 클릭시 다시 돌아감.
        }//삭제if

        //모든 체크박스를 가져오기
        $(".stuChk").each(function(){

            if($(this).is(":checked") == true ){
                console.log("현재 선택된 class 값 : "+$(this).val());
                console.log("현재 선택된 id 값 : "+$(this).parent().parent().attr("id"));
                $("#"+$(this).parent().parent().attr("id")).remove();
            }
        });//each

    });//하단삭제버튼



});//제이쿼리