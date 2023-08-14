from fastapi import APIRouter, Body,  Depends, Path
from schemas.Loan import Loan, example_loan
from services.ServiceLoan import ServiceLoan

router = APIRouter(prefix="/loan", tags=["Loan"])

@router.post("/", response_model=Loan, status_code=201)
async def create_loan(loan: Loan = Body(example=example_loan["post"]), service: ServiceLoan = Depends(ServiceLoan)):
    return service.create_loan(loan)

@router.get("/", response_model=list[Loan], status_code=200)
async def get_loans(service: ServiceLoan = Depends(ServiceLoan)):
    return service.get_loans()

@router.get("/pendiente", response_model=list[Loan], status_code=200)
async def get_pending_loans(service: ServiceLoan = Depends(ServiceLoan)):
    print("hola")
    return service.get_pending_loans()

@router.get("/{loan_id}", response_model=Loan, status_code=200)
async def get_loan(loan_id: int, service: ServiceLoan = Depends(ServiceLoan)):
    return service.get_loan(loan_id)

@router.get("/student/{student_document}", response_model=list[Loan], status_code=200)
async def get_student_loans(student_document: int, service: ServiceLoan = Depends(ServiceLoan)):
    return service.get_loan_by_student(student_document)

@router.get("/admin/{admin_document}", response_model=list[Loan], status_code=200)
async def get_admin_loans(admin_document: int, service: ServiceLoan = Depends(ServiceLoan)):
    return service.get_loans_by_admin(admin_document)
    
@router.put("/{loan_id}",  response_model=Loan, status_code=200, response_description="return loan")
async def return_loan(loan_id: int, service: ServiceLoan = Depends(ServiceLoan)):
    return service.return_loan(loan_id)

@router.get("/day/{day}", response_model=list[Loan], status_code=200)
async def get_loans_by_day(day: str = Path(example="2023-08-13"), service: ServiceLoan = Depends(ServiceLoan)):
    return service.get_loans_by_day(day)
