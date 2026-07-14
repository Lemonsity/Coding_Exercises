let longest_common_substring (s1 : string) (s2 : string) =
  let l1 = String.length s1
  and l2 = String.length s2 in
  let dp = Array.init 2 (fun _ -> Array.init l2 (Fun.const (0, [])))
  and longest = ref []
  in
  for i = 0 to l1 - 1 do
    for j = 0 to l2 - 1 do
      if s1.[i] == s2.[j]
      then
        begin
          begin
            let c = s1.[i] in
            if j = 0
            then dp.(1).(j) <- (1, [c])
            else
              let (old_l, old_s) = dp.(0).(j-1)
              in dp.(1).(j) <- (old_l + 1, c :: old_s)
          end;
          let (cur_l, cur_s) = dp.(1).(j) in
          if cur_l >= List.length (!longest)
          then longest := cur_s
          else ()
        end
      else
        begin
          dp.(1).(j) <- (0, []) ;
        end
    done;
    dp.(0) <- dp.(1);
    dp.(1) <- Array.init l2 (Fun.const (0, []))
  done;
  String.of_seq (List.rev (!longest) |> List.to_seq)
