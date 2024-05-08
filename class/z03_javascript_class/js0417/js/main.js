$(function(){
    // 최초실행 --------------------------------    
    // let no = [1,2,3,4,5,6,7,8,9,10];
    // let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','최현묵','이규원'];
    // let kor = [62,90,64,76,51,89,77,55,73,53];
    // let eng = [70,62,73,54,55,60,67,77,51,100];
    // let math = [81,79,50,83,72,79,82,86,50,94];
    // let total = [213,231,187,213,178,228,226,218,174,247];
    // let avg = [71,77,62.3,71,59.3,76,75.3,72.7,58,82.3];


    //전역변수
    let s_count = 1; //학생번호
    console.log("전역변수 s_count : "+s_count);
    let o_id = 0; //id
    let o_no = 0; //학번
    let o_name = "";
    let o_kor = 0;
    let o_eng = 0;
    let o_math = 0;

    //최초 데이터 불러오기
    $.ajax({
        url:"json/stu_score.json", // ./, /
        data:"",
        type:"get",
        dataType:"json",
        success:function(data){
            //alert("데이터 가져오기 성공");
            console.log(data);
            s_count = data.length;
            console.log("data.length s_count : "+s_count);
            let htmlData = "";
            for (let i=0;i<10;i++){
                htmlData += "<tr id='"+data[i].no+"'>";
                htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+data[i].no+"'></td>";
                htmlData += "<td>"+data[i].no+"</td>";
                htmlData += "<td>"+data[i].name+"</td>";
                htmlData += "<td>"+data[i].kor+"</td>";
                htmlData += "<td>"+data[i].eng+"</td>";
                htmlData += "<td>"+data[i].math+"</td>";
                htmlData += "<td>"+data[i].total+"</td>";
                htmlData += "<td>"+data[i].avg+"</td>";
                htmlData += "<td>"+data[i].rank+"</td>";
                htmlData += "<td><button class='delBtn'>삭제</button></td>";
                htmlData += "</tr>";
            }//for

            // html소스를 tbody 추가
            $("#body").html(htmlData);


        },
        error:function(){ alert("에러"); }

      });//ajax


    // 최초실행 -------------------------------- 


    // 검색버튼 클릭
    $("#searchBtn").click(function(){
        if($("#s_word").val().length<1){
            alert("검색할 학생이름을 입력하셔야 가능합니다.");
            return false;
        }
        
        let s_word = $("#s_word").val();
        console.log("검색어 : "+s_word);


        //최초 데이터 불러오기
        $.ajax({
            url:"json/stu_score.json", // ./, /
            data:"",
            type:"get",
            dataType:"json",
            success:function(data){
                //alert("데이터 가져오기 성공");
                console.log(data);
                s_count = data.length;
                let htmlData = "";
                for (let i=0;i<data.length;i++){
                    // 홍길동.indexOf('홍')
                    if(data[i].name.indexOf(s_word) != -1){ //해당되는 글자가 있으면
                        htmlData += "<tr id='"+data[i].no+"'>";
                        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+data[i].no+"'></td>";
                        htmlData += "<td>"+data[i].no+"</td>";
                        htmlData += "<td>"+data[i].name+"</td>";
                        htmlData += "<td>"+data[i].kor+"</td>";
                        htmlData += "<td>"+data[i].eng+"</td>";
                        htmlData += "<td>"+data[i].math+"</td>";
                        htmlData += "<td>"+data[i].total+"</td>";
                        htmlData += "<td>"+data[i].avg+"</td>";
                        htmlData += "<td>"+data[i].rank+"</td>";
                        htmlData += "<td><button class='delBtn'>삭제</button></td>";
                        htmlData += "</tr>";
                    }//if

                }//for

                // html소스를 tbody 추가
                $("#body").html(htmlData);


            },
            error:function(){ alert("에러"); }

        });//ajax
    });


    //학생입력버튼 클릭
    $("#writeBtn").click(function(){
        if($(".stuChk:checked").length>=1){
            alert("학생입력을 하시려면 체크를 해제하셔야 가능합니다.\n자동 체크해제를 하겠습니다.");
            //체크모두 해제
            $(".stuChk").each(function(){
                $(this).prop("checked",false); //체크해제
            });
            return false;
        }

        $(".p_all").css("display","block");
        $(".p_main h2").text("학생성적입력");
        $("#name").prop("readonly",false);
    });

    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");
        //초기화
        $("#id").val("");
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
    })


    //학생입력,수정 확인 버튼
    $("#confirmBtn").on("click",function(){
        if($("#id").val()==""){ //학생성적입력창 - id value 없는 경우
            // 글자-text() innerText, input-val() value, html() innerHtml
            console.log("이름 : "+$("#name").val());
            
            //공백확인
            if($("#name").val().length<2){
                alert("이름을 입력하셔야 등록이 가능합니다.");
                $("#name").focus();
                return false;
            }
            
            //번호생성은 DB에서 자동으로 부여
            //let i_no = Math.max.apply(null,no)+1;
            //no.push(i_no);
            console.log("confirmBtn s_count : "+s_count);
            s_count = s_count + 1;
            //let i_no = s_count+1;

            console.log("번호 : "+s_count);
            let i_name = $("#name").val(); //String
            let i_kor = Number($("#kor").val());
            let i_eng = Number($("#eng").val());
            let i_math = Number($("#math").val());
            let i_total = i_kor+i_eng+i_math;
            let i_avg = (i_total/3).toFixed(2); //소수점2자리 반올림

            //table tr추가
            let htmlData = "";
            htmlData += "<tr id='"+s_count+"'>";
            htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+s_count+"'></td>";
            htmlData += "<td>"+s_count+"</td>";
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
            $("#id").val("");
            $("#name").val("");
            $("#kor").val("");
            $("#eng").val("");
            $("#math").val("");
            $(".p_all").css("display","none");
        
        }else{ //학생성적수정창 - id value 있는 경우
            //alert("학생성적수정창 클릭");
            o_no =  $("#id").val();
            o_name =  $("#name").val();
            o_kor = Number($("#kor").val());
            o_eng = Number($("#eng").val());
            o_math = Number($("#math").val());
            let o_total = o_kor+o_eng+o_math;
            let o_avg = o_total/3;

            console.log("id : "+o_no);
            console.log("kor : "+o_kor);
            console.log("eng : "+o_eng);
            console.log("math : "+o_math);


            let htmlData = "";
            htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+o_no+"'></td>";
            htmlData += "<td>"+o_no+"</td>";
            htmlData += "<td>"+o_name+"</td>";
            htmlData += "<td>"+o_kor+"</td>";
            htmlData += "<td>"+o_eng+"</td>";
            htmlData += "<td>"+o_math+"</td>";
            htmlData += "<td>"+o_total+"</td>";
            htmlData += "<td>"+o_avg+"</td>";
            htmlData += "<td>"+0+"</td>";
            htmlData += "<td><button class='delBtn'>삭제</button></td>";

            // html소스를 tbody 추가
            $("#"+o_no).html(htmlData);

            //input 초기화
            $("#id").val("");
            $("#name").val("");
            $("#kor").val("");
            $("#eng").val("");
            $("#math").val("");
            $(".p_all").css("display","none");

        }
        
        
    });//학생입력,수정버튼

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




    //학생수정버튼 클릭시
    $("#modifyBtn").click(function(){
        console.log("체크박스에서 체크된 개수 : "+$(".stuChk:checked").length);
        //1명만 선택
        if($(".stuChk:checked").length != 1 ){
            alert("학생 1명만 선택하셔야 수정이 가능합니다.");
            return false;
        }

        //선택된 체크의 데이터 가져오기
        o_id = $(".stuChk:checked").parent();
        o_no = o_id.next().text();
        o_name = o_id.next().next().text();
        o_kor = o_id.next().next().next().text();
        o_eng = o_id.next().next().next().next().text();
        o_math = o_id.next().next().next().next().next().text();
        
        console.log("학번 : "+o_id.next().text());
        
        //수정창 열기
        $(".p_all").css("display","block"); 
        $("#name").prop("readonly",true);
        //수정창 타이틀 변경
        $(".p_main h2").text("학생성적수정");
        $("#id").val(o_no);
        $("#name").val(o_name);
        $("#kor").val(o_kor);
        $("#eng").val(o_eng);
        $("#math").val(o_math);

    });







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