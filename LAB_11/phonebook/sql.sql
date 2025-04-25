-- FIRST TASK
-- get phone by name
create or replace function getNumberByName(pattern TEXT)
returns table(n_firstname varchar(255), n_lastname varchar(255), n_phone varchar(11))
language plpgsql
as $$
begin
    return QUERY
    select firstname, lastname, phone from numbers
    where firstname like pattern || '%';
end;
$$;
-- get phone by numbers of phone 
create or replace function getNumberByPhone(pattern TEXT)
returns table(n_firstname varchar(255), n_lastname varchar(255), n_phone varchar(11))
language plpgsql
as $$
begin
    return query
    select firstname, lastname, phone from numbers
    where phone like pattern || '%';
end;
$$;
-- get phone by lastname
create or replace function getNumberByLastName(pattern TEXT)
returns table(n_firstname varchar(255), n_lastname varchar(255), n_phone varchar(11))
language plpgsql
as $$
begin
    return query
    select firstname, lastname, phone from numbers
    where lastname like pattern || '%';
end;
$$;


-- SECOND TASK
create or replace procedure createPhone(n_firstName varchar(255), n_lastName varchar(255), n_phone varchar(11))
language plpgsql as $$
declare
    phoneId text;
begin 
    select id into phoneId
    from numbers where phone = n_phone or firstname = n_firstName;

    if phoneId is null then insert into numbers (firstname, lastname, phone) values (n_firstName, n_lastName, n_phone);
    else update numbers set firstname = n_firstName, lastname = n_lastName, phone = n_phone where phone = n_phone or firstname = n_firstName;
    end if;
end;
$$; 

call createPhone('islam', 'kabden', '87779402149');


-- THIRD TASK
create or replace procedure createUsers(users JSON)
language plpgsql as $$
declare
    u JSON;
    v_first TEXT;
    v_last TEXT;
    v_phone TEXT;
begin 
    for u in select * from json_array_elements(users)
    loop
        -- save name, last name and phone into variables  
        v_first := u->>'firstName';   
        v_last := u->>'lastName';
        v_phone := u->>'phone'; 
        if length(v_phone) = 11 then  
            call createPhone(v_first, v_last, v_phone);
        else
            raise notice 'Number (%) is not valid',  v_phone;
        end if;
    end loop;
end;
$$;

call createUsers('[
    {"firstName": "Islam", "lastName": "Kabden", "phone": "87001234567"},
    {"firstName": "Aliya", "lastName": "Nurzhanova", "phone": "1"},
    {"firstName": "Dana", "lastName": "Tulegenova", "phone": "87770001122"},
    {"firstName": "Arman", "lastName": "Beketov", "phone": "87771234567"},
    {"firstName": "Aruzhan", "lastName": "Kairatkyzy", "phone": "87005556677"}
]')

-- FORTH TASK

create or replace function pagination(lim int, offs int)
returns table(n_firstname varchar(255), n_lastname varchar(255), phone varchar(11)) as $$
begin
    return query
    select firstname, lastname, phone from numbers order by id limit lim offset offs;
end;
$$ language plpgsql;

select * from pagination(4, 0);

-- FIFTH TASK

create or replace procedure deleteUserByPhone(n_phone varchar(11))
language plpgsql as $$
begin 
    delete from numbers where phone = n_phone;
end;
$$;

call deleteUserByPhone('87773454323');
