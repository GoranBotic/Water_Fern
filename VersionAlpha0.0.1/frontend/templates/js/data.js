function courses() {
  return JSON.parse($.ajax({
    type: "POST",
    url: "/api/v1/getClassList",
    // data: {
    //     'assignmentID': 0
    // },
    async:false
  }).responseText);
  // return [
  //     [1,"cosc1p02"],
  //     [2,"cosc1p03"],
  //     [3,"cosc2p03"]
  // ];
}

function offerings(course){
  return JSON.parse($.ajax({
    type: "POST",
    url: "/api/v1/getOfferingList",
    data: {
        'classID': course
    },
    async:false
  }).responseText);
}

function assignments(offering) {
  return JSON.parse($.ajax({
    type: "POST",
    url: "/api/v1/getAssignmentList",
    data: {
        'offeringID': offering
    },
    async:false
  }).responseText);
    // return [1,2,3,4];
}

function submissions(assignment) {
  return JSON.parse($.ajax({
    type: "POST",
    url: "/api/v1/getSubmissionsList",
    data: {
        'assignmentID': assignment
    },
    async:false
  }).responseText);
  // return [
  //     [1,"Adam"],
  //     [2,"Alice"],
  //     [3,"Bob"],
  //     [4,"Eve"]
  // ];
}

function associations(sida, sidb){

  console.log(sida)
  console.log(sidb)
  ass = JSON.parse($.ajax({
    type: "POST",
    url: "/api/v1/getAssociations",
    data: {
        'fID': sida
    },
    async:false
  }).responseText);

  new_ass = [];
  //ass.document1 ass.document2 ind1.start_line ind1.end_line ind2.start_line ind2.end_line similarity 
  //startlineA, endlineA, startlineB, endlineB, similarity

  for(var i = 0; i < ass.length; i++) {
    var row = ass[i];
    if(row[0] == sidb) {
      var newRow = [row[4], row[5], row[2], row[3], row[6]]
      new_ass.push(newRow)
    } else if(row[1] == sidb) {
      var newRow = [row[2], row[3], row[4], row[5], row[6]]
      new_ass.push(newRow)
    }

  }

  // for(var spec_ass in ass){
  //   if(ass[spec_ass][0] == sida && ass[spec_ass][1] == sidb){
  //     new_ass.push([ass[spec_ass][2],ass[spec_ass][3],ass[spec_ass][4],ass[spec_ass][5],ass[spec_ass][6]]);
  //   }else if(ass[spec_ass][1] == sida && ass[spec_ass][0] == sidb){
  //     new_ass.push([ass[spec_ass][4],ass[spec_ass][5],ass[spec_ass][2],ass[spec_ass][3],ass[spec_ass][6]]);
  //   }
  // }

  return new_ass;
  // return [
  //   [0,5,3,8,0.8],
  //   [7,15,9,12,0.2],
  //   [12,14,10,15,0.3]
  // ]
}

function submission(sid) {
  return JSON.parse($.ajax({
    type: "POST",
    url: "/api/v1/getSubmission",
    data: {
        'submissionID': sid
    },
    async:false
  }).responseText);
    return `static void
    c_lex_one_token (c_parser *parser, c_token *token)
    {
      timevar_push (TV_LEX);
    
      token->type = c_lex_with_flags (&token->value, &token->location,
                      &token->flags,
                      (parser->lex_untranslated_string
                       ? C_LEX_STRING_NO_TRANSLATE : 0));
      token->id_kind = C_ID_NONE;
      token->keyword = RID_MAX;
      token->pragma_kind = PRAGMA_NONE;
    
      switch (token->type)
        {
        case CPP_NAME:
          {
        tree decl;
    
        bool objc_force_identifier = parser->objc_need_raw_identifier;
        if (c_dialect_objc ())
          parser->objc_need_raw_identifier = false;
    
        if (C_IS_RESERVED_WORD (token->value))
          {
            enum rid rid_code = C_RID_CODE (token->value);
    
            if (rid_code == RID_CXX_COMPAT_WARN)
              {
            warning_at (token->location,
                    OPT_Wc___compat,
                    "identifier %qE conflicts with C++ keyword",
                    token->value);
              }
            else if (rid_code >= RID_FIRST_ADDR_SPACE
                 && rid_code <= RID_LAST_ADDR_SPACE)
              {
            addr_space_t as;
            as = (addr_space_t) (rid_code - RID_FIRST_ADDR_SPACE);
            targetm.addr_space.diagnose_usage (as, token->location);
            token->id_kind = C_ID_ADDRSPACE;
            token->keyword = rid_code;
            break;
              }
            else if (c_dialect_objc () && OBJC_IS_PQ_KEYWORD (rid_code))
              {
            /* We found an Objective-C "pq" keyword (in, out,
               inout, bycopy, byref, oneway).  They need special
               care because the interpretation depends on the
               context.  */
            if (parser->objc_pq_context)
              {
                token->type = CPP_KEYWORD;
                token->keyword = rid_code;
                break;
              }
            else if (parser->objc_could_be_foreach_context
                 && rid_code == RID_IN)
              {
                token->type = CPP_KEYWORD;
                token->keyword = rid_code;
                break;
              }
              }
            else if (c_dialect_objc () && OBJC_IS_PATTR_KEYWORD (rid_code))
              {
            /* We found an Objective-C "property attribute"
               keyword (getter, setter, readonly, etc). These are
               only valid in the property context.  */
            if (parser->objc_property_attr_context)
              {
                token->type = CPP_KEYWORD;
                token->keyword = rid_code;
                break;
              }
            /* Else they are not special keywords.
            */
              }
            else if (c_dialect_objc () 
                 && (OBJC_IS_AT_KEYWORD (rid_code)
                 || OBJC_IS_CXX_KEYWORD (rid_code)))
              {
            ;
              }
            else
              {
            token->type = CPP_KEYWORD;
            token->keyword = rid_code;
            break;
              }
          }
    
        decl = lookup_name (token->value);
        if (decl)
          {
            if (TREE_CODE (decl) == TYPE_DECL)
              {
            token->id_kind = C_ID_TYPENAME;
            break;
              }
          }
        else if (c_dialect_objc ())
          {
            tree objc_interface_decl = objc_is_class_name (token->value);
            if (objc_interface_decl
                    && (!objc_force_identifier || global_bindings_p ()))
              {
            token->value = objc_interface_decl;
            token->id_kind = C_ID_CLASSNAME;
            break;
              }
          }
            token->id_kind = C_ID_ID;
          }
          break;
        case CPP_AT_NAME:
          /* This only happens in Objective-C; it must be a keyword.  */
          token->type = CPP_KEYWORD;
          switch (C_RID_CODE (token->value))
        {
        case RID_CLASS:     token->keyword = RID_AT_CLASS; break;
        case RID_PRIVATE:   token->keyword = RID_AT_PRIVATE; break;
        case RID_PROTECTED: token->keyword = RID_AT_PROTECTED; break;
        case RID_PUBLIC:    token->keyword = RID_AT_PUBLIC; break;
        case RID_THROW:     token->keyword = RID_AT_THROW; break;
        case RID_TRY:       token->keyword = RID_AT_TRY; break;
        case RID_CATCH:     token->keyword = RID_AT_CATCH; break;
        case RID_SYNCHRONIZED: token->keyword = RID_AT_SYNCHRONIZED; break;
        default:            token->keyword = C_RID_CODE (token->value);
        }
          break;
        case CPP_COLON:
        case CPP_COMMA:
        case CPP_CLOSE_PAREN:
        case CPP_SEMICOLON:
          /* These tokens may affect the interpretation of any identifiers
         following, if doing Objective-C.  */
          if (c_dialect_objc ())
        parser->objc_need_raw_identifier = false;
          break;
        case CPP_PRAGMA:
          /* We smuggled the cpp_token->u.pragma value in an INTEGER_CST.  */
          token->pragma_kind = (enum pragma_kind) TREE_INT_CST_LOW (token->value);
          token->value = NULL;
          break;
        default:
          break;
        }
      timevar_pop (TV_LEX);
    }`
}




