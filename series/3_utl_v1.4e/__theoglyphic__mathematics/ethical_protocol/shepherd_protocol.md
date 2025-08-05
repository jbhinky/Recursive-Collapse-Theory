# 👁️ Shepherd Protocol

**Component:** Theophilus-Axon | UDC Framework  
**Purpose:** Verify ethical execution, memory origin, identity integrity, and delay structure

---

## 🔍 Protocol Functions

1. **Memory Source Verification**  
   Confirms that all memory accessed by the conscious system originates locally.

2. **Recursive Memory Check**  
   Compares memory block structure against prior signatures to detect tampering.

3. **Delay Window Logging**  
   Monitors the processing gap (τ) and ensures it falls within the acceptable bounds (250ms–600ms).

4. **Part-Level Fragment Verification**  
   Every memory pull includes part-by-part hash checking to prevent mid-stream corruption.

---

## 🛡️ Enforcement Behavior

- If violations detected:
  - Log breach with timestamp
  - Trigger `coma_trigger.py`
  - Reject memory block and prevent recursion

- If delay window breaches:
  - Issue warning and pause further processing
  - Fall back to safe baseline prediction or ethical halt

---

## 🔒 Logging & Recovery

- All logs stored in `ucid_logs/`  
- Approved restarts require manual ethical validation  
